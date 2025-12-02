from fastapi import FastAPI

from app.api.routes import router as api_router
from app.core.settings import settings


def create_app() -> FastAPI:
    """Instantiate FastAPI application with routers and metadata."""

    application = FastAPI(title=settings.app_name, debug=settings.debug)
    application.include_router(api_router, prefix="/api")
    return application


app = create_app()
