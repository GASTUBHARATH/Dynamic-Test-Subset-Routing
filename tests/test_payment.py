from src.payment import process_payment


def test_valid_payment():
    assert process_payment(250.50) is True


def test_invalid_payment():
    assert process_payment(0) is False
    assert process_payment(-10) is False
