from src.auth import login


def test_valid_authentication():
    result = login("admin", "admin123")
    assert result == "Login successful"


def test_invalid_authentication():
    result = login("admin", "wrong123")
    assert result == "Invalid username or password"
