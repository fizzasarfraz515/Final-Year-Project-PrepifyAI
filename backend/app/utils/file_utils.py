from pathlib import Path


def save_upload(file_path: Path, data: bytes) -> Path:
    """Persist uploaded file bytes to disk."""

    file_path.parent.mkdir(parents=True, exist_ok=True)
    file_path.write_bytes(data)
    return file_path
