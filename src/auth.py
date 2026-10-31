def login(username, password):
    """
    Authenticate a user using username and password.
    """

    if username == "admin" and password == "admin123":
        return "Login successful"

    if not username or not password:
        return "Username and password are required"

    return "Invalid username or password"