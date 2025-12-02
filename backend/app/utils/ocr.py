class OCRService:
    """Thin wrapper around OCR engine (e.g., Tesseract)."""

    def extract_text(self, image_bytes: bytes) -> str:
        # TODO: integrate pytesseract
        return "extracted text"
