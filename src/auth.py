"""Simple authentication helpers."""


def authenticate(username: str, password: str) -> bool:
    """Return whether the supplied credentials are valid."""
    return bool(username and password and username == "student" and password == "python123")
