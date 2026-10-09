# business_rules.py
# Author: Ariadna Hernandez

APPROVAL_LIMIT = 1000


def calculate_total(price: float, quantity: int) -> float:
    """Return total cost including 7% tax."""
    return price * quantity * 1.07


def requires_review(amount: float) -> bool:
    """Return True if amount exceeds the approval limit."""
    return amount > APPROVAL_LIMIT


def get_approval_tier(amount: float) -> str:
    """Return the approval routing tier."""
    if amount <= 500:
        return "auto"
    elif amount <= 2000:
        return "manager"
    else:
        return "director"


def apply_discount(price: float, pct: float) -> float:
    """Return price after discount. pct is 0-100."""
    return price * (1 - pct / 100)


# main.py
from business_rules import (
    calculate_total,
    requires_review,
    get_approval_tier,
    apply_discount,
)

price, qty = 450.00, 3
total = calculate_total(price, qty)

print(f"Total:          ${total:.2f}")
print(f"Requires review: {requires_review(total)}")
print(f"Approval tier:   {get_approval_tier(total)}")
print(f"10% discount:    ${apply_discount(price, 10):.2f}")
