from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import settings
from app.routers import upload_router
from app.models.schemas import HealthResponse
from app.services.hai_service import HaiNougatService


def create_application() -> FastAPI:
    """
    Create and configure FastAPI application.

    Returns:
        FastAPI: Configured application instance
    """
    application = FastAPI(
        title=settings.PROJECT_NAME,
        version=settings.VERSION,
        description="Backend API for HaiNougat PDF processing service",
        docs_url=f"{settings.API_V1_PREFIX}/docs",
        redoc_url=f"{settings.API_V1_PREFIX}/redoc",
        openapi_url=f"{settings.API_V1_PREFIX}/openapi.json"
    )

    # Configure CORS
    application.add_middleware(
        CORSMiddleware,
        allow_origins=settings.CORS_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Include routers
    application.include_router(
        upload_router,
        prefix=settings.API_V1_PREFIX
    )

    return application


app = create_application()


@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "HaiNougat API",
        "version": settings.VERSION,
        "docs": f"{settings.API_V1_PREFIX}/docs"
    }


@app.get(f"{settings.API_V1_PREFIX}/health", response_model=HealthResponse)
async def health_check() -> HealthResponse:
    """
    Health check endpoint for the entire application.

    Returns:
        HealthResponse: Application health status
    """
    return HealthResponse(
        status="healthy",
        version=settings.VERSION,
        hepai_configured=HaiNougatService.validate_api_key()
    )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "app.main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=True
    )
