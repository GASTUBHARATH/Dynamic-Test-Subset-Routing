
"""
Payment module for Dynamic Test-Subset Routing.
"""


def process_payment(amount):
    """
    Validate and process a payment.

    Args:
        amount: Payment amount.

    Returns:
        Payment result message.
    """

    if amount <= 0:
        return "Invalid payment amount"

    if amount > 100000:
        return "Payment amount exceeds the allowed limit"

    return "Payment successful"
