from src.auth import authenticate


def test_valid_authentication():
    assert authenticate("student", "python123") is True


def test_invalid_authentication():
    assert authenticate("student", "wrong-password") is False
