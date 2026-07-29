import os
from typing import Optional

from constants import ALLOWED_MIME_TYPES


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
