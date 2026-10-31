
"""
User management module for Dynamic Test-Subset Routing.
"""


def create_user(name, email):
    """
    Create a user profile after validating details.

    Returns:
        Dictionary containing user details if valid.
        None if required details are missing.
    """

    if not name or not email:
        return None

    if "@" not in email:
        return None

    return {
        "name": name,
        "email": email
    }

