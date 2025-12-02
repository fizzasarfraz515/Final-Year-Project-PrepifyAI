class EmbeddingModel:
    """Wrapper around sentence-transformer embeddings."""

    def encode(self, text: str) -> list[float]:
        # TODO: integrate real transformer model
        return [float(len(text))]
