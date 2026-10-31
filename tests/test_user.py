from src.user import create_user


def test_valid_user_creation():
    assert create_user("Ada Lovelace", "ada@example.com") == {
        "name": "Ada Lovelace",
        "email": "ada@example.com",
    }


def test_invalid_user_creation():
    assert create_user("", "ada@example.com") is None
    assert create_user("Ada", "not-an-email") is None
