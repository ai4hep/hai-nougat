from fastapi import APIRouter, File, UploadFile, HTTPException, Depends
import traceback
import asyncio

from app.models.schemas import UploadResponse, ErrorResponse
from app.services.pdf_service import PDFProcessor
from app.services.hai_service import HaiNougatService
from app.utils.limiter import ConcurrencyLimiter
from app.utils.validators import validate_file_size
from app.config import settings

router = APIRouter(prefix="/upload", tags=["upload"])

# Create semaphore for concurrency limiting
semaphore = asyncio.Semaphore(settings.MAX_CONCURRENT_REQUESTS)


@router.post(
    "",
    response_model=UploadResponse,
    responses={
        400: {"model": ErrorResponse, "description": "Invalid file"},
        413: {"model": ErrorResponse, "description": "File too large"},
        429: {"model": ErrorResponse, "description": "Too many requests"},
        500: {"model": ErrorResponse, "description": "Processing error"},
    }
)
async def upload_pdf(file: UploadFile = File(...)) -> UploadResponse:
    """
    Upload and process a PDF file using HaiNougat model.

    Args:
        file: PDF file to process

    Returns:
        UploadResponse: Processing result with extracted content

    Raises:
        HTTPException: Various error conditions
    """
    # Use concurrency limiter
    async with ConcurrencyLimiter(semaphore):
        # Validate content type
        if file.content_type != 'application/pdf':
            raise HTTPException(
                status_code=400,
                detail="File must be a PDF document (application/pdf)"
            )

        # Read file content
        content = await file.read()

        # Validate file size
        validate_file_size(len(content))

        temp_pdf_path = None

        try:
            # Create temporary PDF file
            temp_pdf_path = PDFProcessor.create_temp_pdf(
                content=content,
                filename=file.filename or "uploaded.pdf"
            )

            # Process with HaiNougat
            processed_content = await HaiNougatService.process_pdf(temp_pdf_path)

            return UploadResponse(
                message="File processed successfully",
                content=processed_content,
                filename=file.filename
            )

        except HTTPException:
            # Re-raise HTTP exceptions
            raise

        except Exception as e:
            # Log and raise internal server error
            traceback.print_exc()
            raise HTTPException(
                status_code=500,
                detail=f"Failed to process PDF: {str(e)}"
            )

        finally:
            # Cleanup temporary file
            if temp_pdf_path:
                PDFProcessor.cleanup_temp_file(temp_pdf_path)


@router.get("/health")
async def health_check():
    """
    Health check endpoint for upload service.
    """
    return {
        "status": "healthy",
        "service": "upload",
        "max_concurrent": settings.MAX_CONCURRENT_REQUESTS
    }
