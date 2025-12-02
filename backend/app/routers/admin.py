from fastapi import APIRouter, UploadFile

router = APIRouter(tags=["admin"])


@router.post("/textbooks/upload")
async def upload_textbook(file: UploadFile) -> dict[str, str]:
    # Placeholder response until ingestion pipeline is wired
    return {"filename": file.filename, "status": "queued"}


@router.post("/questions/{question_id}/approve")
async def approve_question(question_id: str) -> dict[str, str]:
    return {"question_id": question_id, "status": "approved"}
