import logging
import os

from dotenv import load_dotenv
from fastapi import FastAPI, File, HTTPException, UploadFile
from fastapi.middleware.cors import CORSMiddleware

from constants import (
    APP_DESCRIPTION,
    APP_TITLE,
    APP_VERSION,
    CORS_ALLOW_CREDENTIALS,
    CORS_ALLOW_HEADERS,
    CORS_ALLOW_METHODS,
    DEFAULT_CORS_ORIGINS,
    MAX_UPLOAD_SIZE_BYTES,
)
from services import GEMINI_API_KEY, GEMINI_MODEL, generate_content_with_retry
from utils import resolve_mime_type

load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("medi-backend")

app = FastAPI(
    title=APP_TITLE,
    description=APP_DESCRIPTION,
    version=APP_VERSION,
)


def _resolve_cors_origins() -> list[str]:
    """
    Reads CORS_ORIGINS from the environment as a comma-separated list
    (e.g. "https://app.example.com,https://staging.example.com").
    Falls back to DEFAULT_CORS_ORIGINS (local Next.js dev) if unset/empty.
    """
    raw = os.environ.get("CORS_ORIGINS", "")
    origins = [origin.strip() for origin in raw.split(",") if origin.strip()]
    return origins or DEFAULT_CORS_ORIGINS


# Enable CORS for the Next.js / React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=_resolve_cors_origins(),
    allow_credentials=CORS_ALLOW_CREDENTIALS,
    allow_methods=CORS_ALLOW_METHODS,
    allow_headers=CORS_ALLOW_HEADERS,
)


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
    if len(file_bytes) > MAX_UPLOAD_SIZE_BYTES:
        raise HTTPException(
            status_code=413,
            detail=f"Uploaded file exceeds the maximum allowed size of {MAX_UPLOAD_SIZE_BYTES // (1024 * 1024)}MB.",
        )

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
