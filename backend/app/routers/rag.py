from fastapi import APIRouter

from app.services.qna_engine import QnAEngine

router = APIRouter(tags=["rag"])
engine = QnAEngine()


@router.post("/generate")
async def generate_question(topic: str, difficulty: str = "medium") -> dict:
    return engine.generate_question(topic=topic, difficulty=difficulty)
