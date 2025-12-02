from fastapi import APIRouter

router = APIRouter()

@router.get("/health", tags=["health"])
async def health_check() -> dict[str, str]:
    """Simple health endpoint to verify service availability."""
    return {"status": "ok"}
