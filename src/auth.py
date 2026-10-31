
"""
Authentication module for Dynamic Test-Subset Routing.
"""


def login(username, password):
    """Authenticate a user."""

    if not username or not password:
        return "Username and password are required"

    if username == "admin" and password == "admin123":
        return "Login successful"

    return "Invalid username or password"


def logout(username):
    """Log out an authenticated user."""

    if not username:
        return "Invalid user"

    return "Logout successful"
