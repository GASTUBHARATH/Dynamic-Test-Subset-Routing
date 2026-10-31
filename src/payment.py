
"""
Payment module for Dynamic Test-Subset Routing.
"""


def process_payment(amount):
    """Validate a payment amount."""

    if amount <= 0 or amount > 100000:
        return False

    return True


def refund_payment(amount):
    """Validate a refund amount."""

    if amount <= 0:
        return False

    return True
