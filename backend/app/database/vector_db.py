from typing import Protocol, Sequence


class VectorStore(Protocol):
    """Protocol describing basic vector store operations required by the app."""

    def add(self, *, embeddings: Sequence[float], metadata: dict) -> str: ...

    def search(self, *, query_embedding: Sequence[float], top_k: int) -> list[dict]: ...


class FaissVectorStore:
    """Placeholder FAISS/Pinecone integration layer."""

    def __init__(self) -> None:
        self._storage: list[dict] = []

    def add(self, *, embeddings: Sequence[float], metadata: dict) -> str:
        record_id = f"vec_{len(self._storage)}"
        self._storage.append({"id": record_id, "embeddings": embeddings, "metadata": metadata})
        return record_id

    def search(self, *, query_embedding: Sequence[float], top_k: int = 5) -> list[dict]:
        # TODO: integrate real vector similarity once FAISS/Pinecone is hooked
        return self._storage[:top_k]


vector_store = FaissVectorStore()
