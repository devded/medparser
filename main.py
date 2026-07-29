import logging
from typing import Optional

from fastapi import FastAPI, File, Header, HTTPException, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse

from constants import (
    APP_DESCRIPTION,
    APP_TITLE,
    APP_VERSION,
    CORS_ALLOW_CREDENTIALS,
    CORS_ALLOW_HEADERS,
    CORS_ALLOW_METHODS,
    CORS_ALLOW_ORIGINS,
    MAX_UPLOAD_SIZE_BYTES,
)
from html_template import HOME_HTML
from services import generate_content_with_retry
from utils import resolve_mime_type

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("medi-backend")

app = FastAPI(
    title=APP_TITLE,
    description=APP_DESCRIPTION,
    version=APP_VERSION,
)

# Open to any origin: auth is via the X-Gemini-Api-Key header, not cookies.
app.add_middleware(
    CORSMiddleware,
    allow_origins=CORS_ALLOW_ORIGINS,
    allow_credentials=CORS_ALLOW_CREDENTIALS,
    allow_methods=CORS_ALLOW_METHODS,
    allow_headers=CORS_ALLOW_HEADERS,
)


@app.get("/", response_class=HTMLResponse)
async def home():
    """
    Returns an interactive HTML overview webpage explaining how to use the API.
    """
    return HTMLResponse(content=HOME_HTML)


@app.get("/health")
async def health_check():
    return {
        "status": "online",
        "required_headers": ["X-Gemini-Api-Key", "X-Gemini-Model"],
    }


@app.post("/extract")
async def extract(
    file: UploadFile = File(...),
    x_gemini_api_key: Optional[str] = Header(None, alias="X-Gemini-Api-Key"),
    x_gemini_model: Optional[str] = Header(None, alias="X-Gemini-Model"),
):
    """
    Extract structured medical report data from an uploaded PDF or image (JPEG/PNG/WEBP/HEIC)
    of a medical report using Gemini. Caller must supply their own Gemini API key and model via
    the X-Gemini-Api-Key and X-Gemini-Model headers — the server holds no Gemini config itself.
    """
    if not x_gemini_api_key:
        raise HTTPException(status_code=401, detail="Missing required 'X-Gemini-Api-Key' header.")
    if not x_gemini_model:
        raise HTTPException(status_code=400, detail="Missing required 'X-Gemini-Model' header.")

    model = x_gemini_model

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
        resp = await generate_content_with_retry(file_bytes, mime_type, x_gemini_api_key, model)
    except HTTPException:
        raise
    except Exception as e:
        err_msg = str(e)
        if "429" in err_msg or "RESOURCE_EXHAUSTED" in err_msg.upper():
            raise HTTPException(
                status_code=429,
                detail="Gemini API rate limit exceeded. Free tier limit reached. Please wait a moment and try again."
            )
        if any(token in err_msg.upper() for token in ("401", "403", "PERMISSION_DENIED", "API_KEY_INVALID", "UNAUTHENTICATED")):
            raise HTTPException(status_code=401, detail="Invalid or unauthorized Gemini API key.")
        raise HTTPException(status_code=502, detail=f"Gemini request failed: {err_msg}")

    # resp.parsed is a typed MedicalReport object
    return {
        "success": True,
        "model_used": model,
        "data": resp.parsed
    }
