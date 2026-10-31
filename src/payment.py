"""Simple payment validation helpers."""


def process_payment(amount: float) -> bool:
    """Return whether a payment amount is valid."""
    return isinstance(amount, (int, float)) and not isinstance(amount, bool) and amount > 0
