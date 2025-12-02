from fastapi import APIRouter

from app.routers import admin, auth, prediction, rag, students


def get_api_router() -> APIRouter:
    router = APIRouter()

    router.include_router(auth.router, prefix="/auth")
    router.include_router(students.router, prefix="/students")
    router.include_router(admin.router, prefix="/admin")
    router.include_router(rag.router, prefix="/rag")
    router.include_router(prediction.router, prefix="/prediction")

    @router.get("/health", tags=["health"])
    async def health_check() -> dict[str, str]:
        return {"status": "ok"}

    return router
