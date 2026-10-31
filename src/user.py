
"""
User management module for Dynamic Test-Subset Routing.
"""


def create_user(name, email):
    """
    Create a user profile after validating details.
    """

    if not name or not email:
        return "Name and email are required"

    if "@" not in email:
        return "Invalid email address"

    return {
        "name": name,
        "email": email,
        "status": "User created successfully"
    }
