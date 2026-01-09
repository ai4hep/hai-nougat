import asyncio
import base64
from functools import partial
from typing import Dict, Any
import sys
import os
from pathlib import Path
from hepai import HepAI, RemoteModel


# Add parent directory to path to import hai_model
parent_dir = Path(__file__).parent.parent.parent.parent
sys.path.insert(0, str(parent_dir))

from hai_model import HaiModel
from app.config import settings


class HaiNougatService:
    """
    Service for interacting with HaiNougat model via HepAI platform.
    """

    @staticmethod
    async def process_pdf(pdf_path: str) -> str:
        """
        Process PDF file using HaiNougat model.

        Args:
            pdf_path: Path to PDF file

        Returns:
            str: Processed content from HaiNougat model

        Raises:
            Exception: If processing fails
        """
        # loop = asyncio.get_running_loop()

        # Create partial function with all parameters
        # inference_func = partial(
        #     HaiModel.inference,
        #     model=settings.HEPAI_MODEL,
        #     timeout=settings.HEPAI_TIMEOUT,
        #     stream=False,
        #     pdf_path=pdf_path,
        #     url=settings.HEPAI_API_URL,
        #     api_key=settings.HEPAI_API_KEY
        # )

        # # Execute in thread pool to avoid blocking
        # result = await loop.run_in_executor(None, inference_func)

        model: RemoteModel = HepAI(
            base_url=settings.HEPAI_API_V2_URL,
        ).connect_to(settings.HEPAI_MODEL)

        print(model.worker_info)  # Get worker info.
        print(model.functions)  # Get all remote callable functions.
        print(model.function_details)  # Get all remote callable function details.

        # Call the `custom_method` of the remote model.
        with open(pdf_path, "rb") as f:
            bytes_ = f.read()
        pdfbin = base64.b64encode(bytes_).decode()
        result = model.inference(
            api_key=settings.HEPAI_API_KEY,
            stream=False,
            timeout=60,
            pdfbin=pdfbin,
        )

        return result

    @staticmethod
    def validate_api_key() -> bool:
        """
        Check if HepAI API key is configured.

        Returns:
            bool: True if API key is set, False otherwise
        """
        return bool(settings.HEPAI_API_KEY)
