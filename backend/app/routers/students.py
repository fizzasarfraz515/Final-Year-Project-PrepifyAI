from fastapi import APIRouter

router = APIRouter(tags=["students"])


@router.get("/{student_id}/progress")
async def get_progress(student_id: str) -> dict:
    # TODO: integrate with adaptive engine once implemented
    return {"student_id": student_id, "progress": []}


@router.get("/{student_id}/analytics")
async def get_analytics(student_id: str) -> dict:
    return {"student_id": student_id, "strengths": [], "weaknesses": []}
