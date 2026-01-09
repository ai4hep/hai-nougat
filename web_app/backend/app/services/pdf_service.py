import tempfile
import os
from typing import BinaryIO
from werkzeug.utils import secure_filename
from app.utils.validators import validate_pdf_content


class PDFProcessor:
    """
    Service for processing PDF files.
    """

    @staticmethod
    def create_temp_pdf(content: bytes, filename: str) -> str:
        """
        Create a temporary PDF file from uploaded content.

        Args:
            content: PDF file content in bytes
            filename: Original filename

        Returns:
            str: Path to temporary PDF file
        """
        # Validate PDF content
        validate_pdf_content(content)

        # Secure the filename
        safe_filename = secure_filename(filename)

        # Create temporary file
        temp_fd, temp_path = tempfile.mkstemp(
            prefix=f"{safe_filename}_",
            suffix='.pdf'
        )

        # Write content to temp file
        with os.fdopen(temp_fd, 'wb') as temp_file:
            temp_file.write(content)

        return temp_path

    @staticmethod
    def cleanup_temp_file(file_path: str) -> None:
        """
        Remove temporary file.

        Args:
            file_path: Path to file to remove
        """
        try:
            if os.path.exists(file_path):
                os.remove(file_path)
        except Exception as e:
            print(f"Warning: Failed to remove temp file {file_path}: {e}")
