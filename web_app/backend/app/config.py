import os
from typing import List, Union
from pydantic import field_validator
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings"""

    # API settings
    API_V1_PREFIX: str = "/api/v1"
    PROJECT_NAME: str = "HaiNougat API"
    VERSION: str = "1.0.0"

    # CORS settings
    CORS_ORIGINS: Union[str, List[str]] = "http://localhost:3000,http://localhost:5173"

    @field_validator("CORS_ORIGINS", mode="before")
    @classmethod
    def parse_cors_origins(cls, v):
        """Parse CORS origins from comma-separated string or list"""
        if isinstance(v, str):
            return [origin.strip() for origin in v.split(",") if origin.strip()]
        return v

    # HepAI settings
    HEPAI_API_KEY: str = os.environ.get("HEPAI_API_KEY", "")
    HEPAI_API_URL: str = "https://aiapi.ihep.ac.cn"
    HEPAI_API_V2_URL: str = "https://aiapi.ihep.ac.cn/apiv2"
    HEPAI_MODEL: str = "hepai/hainougat"
    HEPAI_TIMEOUT: int = 3000

    # Upload settings
    MAX_CONCURRENT_REQUESTS: int = 5
    UPLOAD_MAX_SIZE: int = 10 * 1024 * 1024  # 10MB
    ALLOWED_EXTENSIONS: List[str] = [".pdf"]

    # Server settings
    HOST: str = "0.0.0.0"
    PORT: int = 8000

    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()
