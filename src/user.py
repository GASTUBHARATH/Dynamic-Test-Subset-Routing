"""Simple user-profile helpers."""

import re


def create_user(name: str, email: str) -> dict[str, str] | None:
    """Create a user profile when both fields have valid values."""
    if not name.strip() or not re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", email):
        return None
    return {"name": name.strip(), "email": email.strip()}
