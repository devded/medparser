import asyncio
import logging
import os

from dotenv import load_dotenv
from fastapi import HTTPException
from google import genai
from google.genai import types

from constants import DEFAULT_MAX_RETRIES, INITIAL_RETRY_DELAY_SECONDS, PROMPT, RETRY_BACKOFF_FACTOR
from schemas import MedicalReport

load_dotenv()

logger = logging.getLogger("medi-backend")

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "")
GEMINI_MODEL = os.environ.get("GEMINI_MODEL", "gemini-3.6-flash")

client = None
if GEMINI_API_KEY:
    client = genai.Client(api_key=GEMINI_API_KEY)
else:
    logger.warning("GEMINI_API_KEY environment variable not set.")


async def generate_content_with_retry(file_bytes: bytes, mime_type: str, max_retries: int = DEFAULT_MAX_RETRIES):
    """
    Executes Gemini API content generation with exponential backoff on 429 (Rate Limit) errors.
    """
    if not GEMINI_API_KEY or client is None:
        raise HTTPException(
            status_code=500,
            detail="GEMINI_API_KEY is not configured on the server. Please set GEMINI_API_KEY environment variable."
        )

    delay = INITIAL_RETRY_DELAY_SECONDS
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
                delay *= RETRY_BACKOFF_FACTOR
            else:
                logger.error(f"Gemini API call failed permanently on attempt {attempt}: {err_str}")
                raise e

    raise last_exception or Exception("Failed after maximum retries")
