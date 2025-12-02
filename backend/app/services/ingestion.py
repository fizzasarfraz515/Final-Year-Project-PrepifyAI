class IngestionPipeline:
    """Handles textbook ingestion, OCR, and embedding generation."""

    def enqueue_textbook(self, *, filename: str) -> dict[str, str]:
        return {"filename": filename, "status": "pending"}
