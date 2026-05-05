"""Objective:
You are building a billing module for a small grocery store
called "QuickMart". The system takes a list of purchased items
and generates a clean formatted receipt with tax and discount
applied.

cart = [
    ("Milk",       2,  1.50),
    ("Bread",      1,  2.30),
    ("Eggs",       3,  0.99),
    ("Butter",     1,  3.75),
    ("Orange Juice", 2, 2.10),
]

TAX_RATE      = 0.08   # 8%
DISCOUNT_RATE = 0.05   # 5% for orders above $10
STORE_NAME    = "QuickMart"
CASHIER       = "Ahmed"

Task 1 — Write calculate_totals(cart) that:
Loops through cart — each item is a tuple of (name, quantity, price)
Calculates subtotal for each item: quantity * price
Returns (subtotal, tax, discount, grand_total) as a tuple
Apply discount only if subtotal > 10, otherwise discount = 0

Task 2 — Write generate_receipt(cart, totals) that:
Unpacks the totals tuple
Prints the receipt
"""

cart = [
    ("Milk",         2, 1.50),
    ("Bread",        1, 2.30),
    ("Eggs",         3, 0.99),
    ("Butter",       1, 3.75),
    ("Orange Juice", 2, 2.10),
]
TAX_RATE      = 0.08
DISCOUNT_RATE = 0.05
STORE_NAME    = "QuickMart"
CASHIER       = "Ahmed"


def calculate_totals(cart):
    dictionary = {}
    for name, quantity, price in cart:
        dictionary[name] = round(quantity * price, 2)

    subtotal = round(sum(dictionary.values()), 2)
    discount = round(subtotal * DISCOUNT_RATE, 2) if subtotal > 10 else 0
    discounted = subtotal - discount
    tax = round(discounted * TAX_RATE, 2)
    grand_total = round(discounted + tax, 2)

    return subtotal, tax, discount, grand_total, dictionary


def generate_receipt(cart, totals):
    subtotal, tax, discount, grand_total, dictionary = totals

    print(f"\n{'=' * 32}")
    print(f"{'QUICKMART':^32}")
    print(f"{'Cashier: ' + CASHIER:^32}")
    print(f"{'=' * 32}")
    print(f"{'Item':<16} {'Qty':>4}  {'Price':>8}")
    print(f"{'-' * 32}")

    for name, quantity, price in cart:
        item_total = round(quantity * price, 2)
        print(f"{name:<16} {quantity:>4}  ${item_total:>6.2f}")

    print(f"{'-' * 32}")
    print(f"{'Subtotal':<22} ${subtotal:>6.2f}")
    print(f"{'Discount (5%)':<22}-${discount:>6.2f}")
    print(f"{'Tax (8%)':<22} ${tax:>6.2f}")
    print(f"{'=' * 32}")
    print(f"{'TOTAL':<22} ${grand_total:>6.2f}")
    print(f"{'=' * 32}")
    print(f"{'Thank you for shopping with us!':^32}")


totals = calculate_totals(cart)
generate_receipt(cart, totals)