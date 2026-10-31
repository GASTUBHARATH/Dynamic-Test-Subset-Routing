
"""
Authentication module for Dynamic Test-Subset Routing.
"""


def login(username, password):
    """
    Authenticate a user using username and password.

    Args:
        username: User's login name.
        password: User's password.

    Returns:
        A message indicating the authentication result.
    """

    if not username or not password:
        return "Username and password are required"

    if username == "admin" and password == "admin123":
        return "Login successful"

    return "Invalid username or password"
