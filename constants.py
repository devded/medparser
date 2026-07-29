APP_TITLE = "MediReport AI Extractor API"
APP_DESCRIPTION = "Medical Report Extraction using Gemini 3.6 Flash & FastAPI"
APP_VERSION = "1.0.0"

# Auth is via the X-Gemini-Api-Key header, not cookies, so a wildcard origin is
# safe here and allow_credentials must stay False (invalid combination otherwise).
CORS_ALLOW_ORIGINS = ["*"]
CORS_ALLOW_CREDENTIALS = False
CORS_ALLOW_METHODS = ["*"]
CORS_ALLOW_HEADERS = ["*"]

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

DEFAULT_MAX_RETRIES = 4
INITIAL_RETRY_DELAY_SECONDS = 2.0
RETRY_BACKOFF_FACTOR = 2.0

# 15MB: Gemini's inline generateContent request ceiling is ~20MB total; base64
# encoding inflates raw bytes by ~33%, so 15MB raw leaves headroom for the
# prompt/schema while still covering large multi-page scanned medical PDFs.
MAX_UPLOAD_SIZE_BYTES = 15 * 1024 * 1024
