from typing import Any


def success(data: Any, message: str = "OK") -> dict[str, Any]:
    return {"status": "success", "message": message, "data": data}


def error(message: str, details: Any | None = None) -> dict[str, Any]:
    payload: dict[str, Any] = {"status": "error", "message": message}
    if details is not None:
        payload["details"] = details
    return payload
