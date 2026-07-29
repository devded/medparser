import os
import io
import asyncio
import logging
from typing import List, Optional
from fastapi import FastAPI, UploadFile, File, HTTPException, Response
from fastapi.middleware.cors import CORSMiddleware
from google import genai
from google.genai import types
from pydantic import BaseModel, Field
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("medi-backend")

app = FastAPI(
    title="MediReport AI Extractor API",
    description="Medical Report Extraction using Gemini 3.6 Flash & FastAPI",
    version="1.0.0"
)

# Enable CORS for Next.js / React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Get API key from environment variable
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "")
GEMINI_MODEL = os.environ.get("GEMINI_MODEL", "gemini-3.6-flash")

# Initialize Gemini Client if key exists
client = None
if GEMINI_API_KEY:
    client = genai.Client(api_key=GEMINI_API_KEY)
else:
    logger.warning("GEMINI_API_KEY environment variable not set.")


# --- Response Schemas ---
class Test(BaseModel):
    name: Optional[str] = Field(None, description="Name of the test or biomarker")
    value: Optional[str] = Field(None, description="Measured result value")
    unit: Optional[str] = Field(None, description="Unit of measurement (e.g. mg/dL, g/dL)")
    reference_range: Optional[str] = Field(None, description="Normal reference range (e.g. 13.5 - 17.5)")
    is_abnormal: Optional[bool] = Field(None, description="True if result is flagged as abnormal or out of reference range")
    category: Optional[str] = Field(None, description="Category of test (e.g., Hematology, Chemistry, Lipids)")


class MedicalReport(BaseModel):
    patient_name: Optional[str] = Field(None, description="Patient full name")
    patient_id: Optional[str] = Field(None, description="Patient ID or MRN if available")
    date: Optional[str] = Field(None, description="Date of test or report")
    lab_name: Optional[str] = Field(None, description="Name of laboratory or clinic")
    doctor_name: Optional[str] = Field(None, description="Ordering physician name")
    clinical_summary: Optional[str] = Field(None, description="Brief summary of key findings and overall health status")
    tests: List[Test] = Field(default_factory=list, description="List of lab tests extracted from the report")


PROMPT = (
    "You are an expert medical data parser. "
    "Extract all lab test results, patient details, and clinical metadata from this medical report document into the specified JSON schema. "
    "Identify whether any test value falls outside the reference range and set 'is_abnormal' to true if flagged or out of range. "
    "Categorize tests logically (e.g. Hematology, Lipid Panel, Metabolic, Thyroid, Liver). "
    "Use null for any field not present in the document."
)

# Accepted upload types: PDF documents and common image formats
ALLOWED_MIME_TYPES = {
    "application/pdf": ".pdf",
    "image/jpeg": (".jpg", ".jpeg"),
    "image/png": ".png",
    "image/webp": ".webp",
    "image/heic": ".heic",
    "image/heif": ".heif",
}


def resolve_mime_type(content_type: Optional[str], filename: str) -> Optional[str]:
    """
    Determines the mime type to send to Gemini based on the upload's declared
    content type, falling back to the filename extension if it's missing/generic.
    """
    if content_type in ALLOWED_MIME_TYPES:
        return content_type

    ext = os.path.splitext(filename.lower())[1]
    for mime, exts in ALLOWED_MIME_TYPES.items():
        if ext == exts or ext in exts:
            return mime

    return None


async def generate_content_with_retry(file_bytes: bytes, mime_type: str, max_retries: int = 4):
    """
    Executes Gemini API content generation with exponential backoff on 429 (Rate Limit) errors.
    """
    if not GEMINI_API_KEY or client is None:
        raise HTTPException(
            status_code=500,
            detail="GEMINI_API_KEY is not configured on the server. Please set GEMINI_API_KEY environment variable."
        )

    delay = 2.0  # Initial retry delay in seconds
    last_exception = None

    for attempt in range(1, max_retries + 1):
        try:
            logger.info(f"Sending extraction request to Gemini ({GEMINI_MODEL}) - Attempt {attempt}/{max_retries}")
            
            resp = await client.aio.models.generate_content(
                model=GEMINI_MODEL,
                contents=[
                    types.Part.from_bytes(data=file_bytes, mime_type=mime_type),
                    PROMPT,
                ],
                config={
                    "response_mime_type": "application/json",
                    "response_schema": MedicalReport,
                },
            )
            return resp
        except Exception as e:
            err_str = str(e)
            last_exception = e
            
            # Check for Rate Limit (429) or transient server errors
            is_rate_limit = "429" in err_str or "RESOURCE_EXHAUSTED" in err_str.upper() or "Quota" in err_str
            is_transient = "503" in err_str or "UNAVAILABLE" in err_str.upper()

            if (is_rate_limit or is_transient) and attempt < max_retries:
                logger.warning(
                    f"Gemini API rate limit/transient error encountered (Attempt {attempt}). "
                    f"Retrying in {delay:.1f} seconds... Error: {err_str}"
                )
                await asyncio.sleep(delay)
                delay *= 2.0  # Exponential backoff
            else:
                logger.error(f"Gemini API call failed permanently on attempt {attempt}: {err_str}")
                raise e

    raise last_exception or Exception("Failed after maximum retries")


@app.get("/health")
async def health_check():
    return {
        "status": "online",
        "model": GEMINI_MODEL,
        "api_key_configured": bool(GEMINI_API_KEY)
    }


@app.post("/extract")
async def extract(file: UploadFile = File(...)):
    """
    Extract structured medical report data from an uploaded PDF or image (JPEG/PNG/WEBP/HEIC)
    of a medical report using Gemini 3.6 Flash.
    """
    mime_type = resolve_mime_type(file.content_type, file.filename or "")
    if mime_type is None:
        raise HTTPException(
            status_code=400,
            detail="Unsupported file type. Please upload a PDF or an image (JPEG, PNG, WEBP, HEIC)."
        )

    file_bytes = await file.read()
    if not file_bytes or len(file_bytes) < 100:
        raise HTTPException(status_code=400, detail="Uploaded file is empty or corrupted.")

    try:
        resp = await generate_content_with_retry(file_bytes, mime_type)
    except HTTPException:
        raise
    except Exception as e:
        err_msg = str(e)
        if "429" in err_msg or "RESOURCE_EXHAUSTED" in err_msg.upper():
            raise HTTPException(
                status_code=429,
                detail="Gemini API rate limit exceeded. Free tier limit reached. Please wait a moment and try again."
            )
        raise HTTPException(status_code=502, detail=f"Gemini request failed: {err_msg}")

    # resp.parsed is a typed MedicalReport object
    return {
        "success": True,
        "model_used": GEMINI_MODEL,
        "data": resp.parsed
    }


# Sample Medical PDF Generator for easy testing
@app.get("/api/sample-pdf/{sample_type}")
async def get_sample_pdf(sample_type: str):
    """
    Generates a synthetic medical PDF (CBC, Lipid Panel, or Metabolic) for quick zero-setup testing.
    """
    try:
        from reportlab.lib.pagesizes import letter
        from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
        from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
        from reportlab.lib import colors

        buffer = io.BytesIO()
        doc = SimpleDocTemplate(buffer, pagesize=letter, rightMargin=36, leftMargin=36, topMargin=36, bottomMargin=36)
        styles = getSampleStyleSheet()
        elements = []

        title_style = ParagraphStyle(
            'ReportTitle',
            parent=styles['Heading1'],
            fontSize=18,
            textColor=colors.HexColor('#1E293B'),
            spaceAfter=12
        )
        
        meta_style = ParagraphStyle(
            'ReportMeta',
            parent=styles['Normal'],
            fontSize=10,
            textColor=colors.HexColor('#475569'),
            leading=14
        )

        if sample_type == "lipid":
            title = "CARDIOVASCULAR & LIPID PANEL REPORT"
            patient = "John Doe | Age: 52 | Male | DOB: 1974-05-12"
            dr = "Dr. Sarah Jenkins, MD (Cardiology)"
            date = "2026-06-15"
            table_data = [
                ["Test Name", "Result", "Units", "Reference Range", "Flag"],
                ["Total Cholesterol", "245", "mg/dL", "< 200", "HIGH"],
                ["Triglycerides", "185", "mg/dL", "< 150", "HIGH"],
                ["HDL Cholesterol", "38", "mg/dL", "> 40", "LOW"],
                ["LDL Cholesterol", "170", "mg/dL", "< 100", "HIGH"],
                ["Non-HDL Cholesterol", "207", "mg/dL", "< 130", "HIGH"],
                ["hs-CRP", "3.2", "mg/L", "< 1.0", "HIGH"],
            ]
        elif sample_type == "metabolic":
            title = "COMPREHENSIVE METABOLIC PANEL (CMP)"
            patient = "Maria Garcia | Age: 41 | Female | DOB: 1985-11-20"
            dr = "Dr. Michael Chen, MD (Internal Medicine)"
            date = "2026-07-02"
            table_data = [
                ["Test Name", "Result", "Units", "Reference Range", "Flag"],
                ["Glucose (Fasting)", "112", "mg/dL", "70 - 99", "HIGH"],
                ["BUN", "18", "mg/dL", "7 - 20", "NORMAL"],
                ["Creatinine", "0.9", "mg/dL", "0.6 - 1.2", "NORMAL"],
                ["Sodium", "141", "mEq/L", "135 - 145", "NORMAL"],
                ["Potassium", "4.2", "mEq/L", "3.5 - 5.1", "NORMAL"],
                ["ALT (SGPT)", "58", "U/L", "7 - 56", "HIGH"],
                ["AST (SGOT)", "32", "U/L", "10 - 40", "NORMAL"],
                ["Calcium", "9.6", "mg/dL", "8.5 - 10.5", "NORMAL"],
            ]
        else: # cbc
            title = "COMPLETE BLOOD COUNT (CBC) WITH DIFFERENTIAL"
            patient = "Alex Rivera | Age: 29 | Non-Binary | DOB: 1997-03-08"
            dr = "Dr. Emily Taylor, MD (Hematology)"
            date = "2026-07-18"
            table_data = [
                ["Test Name", "Result", "Units", "Reference Range", "Flag"],
                ["WBC Count", "7.4", "x10^3/uL", "4.5 - 11.0", "NORMAL"],
                ["RBC Count", "4.8", "x10^6/uL", "4.3 - 5.9", "NORMAL"],
                ["Hemoglobin", "11.2", "g/dL", "13.5 - 17.5", "LOW"],
                ["Hematocrit", "34.5", "%", "41.0 - 50.0", "LOW"],
                ["MCV", "72.0", "fL", "80.0 - 100.0", "LOW"],
                ["Platelet Count", "265", "x10^3/uL", "150 - 450", "NORMAL"],
                ["Neutrophils %", "62.0", "%", "40.0 - 74.0", "NORMAL"],
                ["Lymphocytes %", "28.0", "%", "19.0 - 48.0", "NORMAL"],
            ]

        elements.append(Paragraph("APEX HEALTH DIAGNOSTICS LABORATORY", title_style))
        elements.append(Paragraph(f"<b>Report:</b> {title}<br/><b>Patient:</b> {patient}<br/><b>Ordering Physician:</b> {dr}<br/><b>Date:</b> {date}", meta_style))
        elements.append(Spacer(1, 16))

        t = Table(table_data, colWidths=[160, 70, 80, 120, 70])
        t.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#0F172A')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 10),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
            ('TOPPADDING', (0, 0), (-1, 0), 8),
            ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor('#F8FAFC')),
            ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#CBD5E1')),
            ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
            ('FONTSIZE', (0, 1), (-1, -1), 9),
        ]))
        elements.append(t)
        elements.append(Spacer(1, 20))
        elements.append(Paragraph("<i>Note: This is a synthetic diagnostic report generated for demonstration & test purposes.</i>", meta_style))

        doc.build(elements)
        buffer.seek(0)
        return Response(content=buffer.getvalue(), media_type="application/pdf", headers={"Content-Disposition": f"inline; filename=sample_{sample_type}.pdf"})
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to generate sample PDF: {e}")
