from pydantic import BaseModel
from typing import Optional


class UploadResponse(BaseModel):
    """Response model for PDF upload"""
    message: str
    content: str
    filename: Optional[str] = None


class ErrorResponse(BaseModel):
    """Error response model"""
    detail: str
    status_code: int


class HealthResponse(BaseModel):
    """Health check response"""
    status: str
    version: str
    hepai_configured: bool
