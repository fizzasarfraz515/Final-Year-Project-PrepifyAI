import secrets
from dataclasses import dataclass
from typing import Optional

from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


@dataclass
class UserService:
    """Handles user registration and authentication logic."""

    def authenticate(self, *, username: str, password: str) -> Optional[str]:
        # TODO: replace with DB lookup; this is only a stub
        if username and password:
            return secrets.token_hex(16)
        return None

    def create_user(self, *, username: str, password: str) -> dict:
        hashed = pwd_context.hash(password)
        return {"id": secrets.token_hex(8), "username": username, "password_hash": hashed}
