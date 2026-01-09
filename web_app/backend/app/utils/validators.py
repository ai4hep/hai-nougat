from io import BytesIO
from fastapi import HTTPException
import PyPDF2
from PyPDF2 import PdfReader
from app.config import settings


def is_valid_pdf(file_stream) -> bool:
    """
    Validate if the file is a valid PDF.

    Args:
        file_stream: File stream to validate

    Returns:
        bool: True if valid PDF, False otherwise
    """
    try:
        # Reset stream position
        if hasattr(file_stream, 'seek'):
            file_stream.seek(0)

        # Try to read as PDF
        PdfReader(file_stream)

        # Reset stream position again for further processing
        if hasattr(file_stream, 'seek'):
            file_stream.seek(0)

        return True
    except (PyPDF2.errors.PdfReadError, AssertionError, Exception):
        return False


def validate_file_size(file_size: int) -> None:
    """
    Validate file size against maximum allowed size.

    Args:
        file_size: Size of the file in bytes

    Raises:
        HTTPException: If file size exceeds maximum
    """
    if file_size > settings.UPLOAD_MAX_SIZE:
        max_mb = settings.UPLOAD_MAX_SIZE / (1024 * 1024)
        raise HTTPException(
            status_code=413,
            detail=f"File size exceeds maximum allowed size of {max_mb}MB"
        )


def validate_pdf_content(content: bytes) -> None:
    """
    Validate PDF file content.

    Args:
        content: File content in bytes

    Raises:
        HTTPException: If content is not a valid PDF
    """
    file_stream = BytesIO(content)
    if not is_valid_pdf(file_stream):
        raise HTTPException(
            status_code=400,
            detail="Invalid PDF file. Please upload a valid PDF document."
        )
