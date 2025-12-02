class QnAEngine:
    """Coordinates RAG components to craft exam-ready questions."""

    def generate_question(self, *, topic: str, difficulty: str) -> dict:
        return {
            "question": f"Sample {difficulty} question for {topic}",
            "options": [],
            "answer": None,
        }
