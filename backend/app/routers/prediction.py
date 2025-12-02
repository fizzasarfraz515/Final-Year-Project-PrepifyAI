from fastapi import APIRouter

from app.services.trend_engine import TrendEngine

router = APIRouter(tags=["prediction"])
engine = TrendEngine()


@router.get("/topics")
async def get_high_probability_topics(board: str, subject: str) -> dict:
    return engine.predict_topics(board=board, subject=subject)
