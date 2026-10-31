
"""
Payment module for Dynamic Test-Subset Routing.
"""


def process_payment(amount):
    """
    Validate a payment amount.

    Returns:
        True if payment is valid.
        False if payment is invalid.
    """

    if amount <= 0:
        return False

    if amount > 100000:
        return False

    return True
