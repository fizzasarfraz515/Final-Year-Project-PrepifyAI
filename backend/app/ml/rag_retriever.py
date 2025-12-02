from app.database.vector_db import vector_store
from app.ml.embedding import EmbeddingModel


class RAGRetriever:
    """Fetches top-k textbook chunks for a query."""

    def __init__(self) -> None:
        self.embedding = EmbeddingModel()

    def retrieve(self, query: str, top_k: int = 5) -> list[dict]:
        query_embedding = self.embedding.encode(query)
        return vector_store.search(query_embedding=query_embedding, top_k=top_k)
