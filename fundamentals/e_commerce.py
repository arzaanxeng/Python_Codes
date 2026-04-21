"""
You are a backend developer at an e-commerce company. Your system receives a raw batch
of order records as strings.You must validate Order IDs using regular expressions, store
valid records in a dictionary, and calculate revenue summaries.

The company's Order ID format is: 2 Uppercase Letters + "-" + 3 Digits + "-" + 2 Digits (e.g., OR-102-44).
Define the function
def process_orders(raw_orders):
    ...
    return valid_orders

Input_data:
raw_orders = [
    "OR-102-44|Electronics|1200.00",
    "bad-id|Clothing|89.99",
    "KL-887-12|Groceries|45.50",
    "ZP-01-9|Books|15.00",
    "MN-456-78|Sports|300.00"
]
For each entry, check if the Order ID matches the required format.
If valid, store it in valid_orders dict where the key is the Order ID and the value is a tuple
of (category, amount). Otherwise, print: "Skipping Invalid Order: [ID]". Return the dictionary.

Then define calculate_revenue(valid_orders, tax_rate=0.08) that computes and returns the total
revenue after adding tax for all valid orders.
Main program flow
1. Call process_orders() and store the result.
2. Call calculate_revenue() and print the total.
3. Print each valid order in the format below.
"""
import re
raw_orders = [
    "OR-102-44|Electronics|1200.00",
    "bad-id|Clothing|89.99",
    "KL-887-12|Groceries|45.50",
    "ZP-01-9|Books|15.00",
    "MN-456-78|Sports|300.00"
]

#EXTRACTION VALID AND INVALID DATA
def process_orders(raw_orders):
    data = {}
    invalid_id = []
    id_pattern = re.compile(r"^[A-Z]{2}-\d{3}-\d{2}$")

    for line in raw_orders:
        line_split = line.split("|")
        if len(line_split) != 3:
            continue
        order_id, category, amount = line_split
        amount = float(amount)
        if id_pattern.match(order_id):
            data[order_id] = (category, amount)
        else:
            invalid_id.append(order_id)

    print(invalid_id)
    return data, invalid_id

#REVENUE CALCULATION
def calculate_revenue(valid_orders, invalid_orders , tax_rate=0.08):
    print("--- ORDER PROCESSING STARTED ---")
    for i in range(len(invalid_orders)):
       print(f"Skipping Invalid Order:{invalid_orders[i]}")
    print("--- Processing valid orders ---")
    subtotal = 0.0
    for id, (category, amount) in valid_orders.items():
        print(f"ID:{id:<10} |Category:{category:<12} |Amount:${amount:<12}")
        subtotal += amount
    tax = subtotal * tax_rate
    total = subtotal + tax
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Tax ({tax_rate*100:.0f}%): ${tax:.2f}")
    print(f"Total: ${total:}")

#MAIN
valid_orders , invalid_orders = process_orders(raw_orders)
calculate_revenue(valid_orders , invalid_orders)
