from fastapi import FastAPI

from app.config.settings import settings
from app.routers import get_api_router


def create_app() -> FastAPI:
    """Instantiate FastAPI application with routers and metadata."""

    application = FastAPI(title=settings.app_name, debug=settings.debug)
    application.include_router(get_api_router(), prefix="/api")
    return application


app = create_app()
