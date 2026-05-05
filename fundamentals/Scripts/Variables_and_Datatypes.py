"""Objective:
You are building a backend data management module for a secure
digital banking system called "VaultCore". The system receives
raw user input as strings and must sanitize, convert, and
validate all data before storing it.

raw_data = {
    "user_id"        : "1001",
    "account_balance": "5400.75",
    "is_verified"    : "True",
    "credit_score"   : "742",
    "transaction_ids": "TX001,TX002,TX003,TX004",
    "interest_rate"  : "3.5",
    "account_type"   : "  savings  ",
    "overdraft_limit": "-500",
}

Task 1 — Type Conversion & Sanitization
Write a function sanitize_record(raw_data) that:
Converts user_id to int
Converts account_balance to float
Converts is_verified from string "True"/"False" to actual Python bool
Converts credit_score to int
Strips whitespace from account_type and converts to uppercase
Converts interest_rate to float
Converts overdraft_limit to int
Splits transaction_ids by comma into a list
Returns a new clean dictionary with all converted values

Task 2 — Type Verification
Write a function verify_types(clean_data) that:
Loops through every key-value pair in the clean dictionary
Prints the key, its value, and its type in this format:

user_id          → 1001          | type: int
account_balance  → 5400.75       | type: float
is_verified      → True          | type: bool

Task 3 — Financial Calculations
Write a function calculate_financials(clean_data) that:
Calculates the monthly interest earned:
monthly_interest = account_balance * (interest_rate / 100) / 12
Calculates the maximum withdrawable amount:
max_withdrawal = account_balance + abs(overdraft_limit)
Calculates a risk score:
risk_score = round((credit_score / 850) * 100, 2)
Returns all three as a tuple: (monthly_interest, max_withdrawal, risk_score)


Task 4 — Account Status Report
Write a function generate_report(clean_data, financials) that:
Unpacks the financials tuple into three variables
Checks if credit_score >= 700 → "Excellent", >= 600 → "Good", else → "Poor"
Checks if account_balance > 0 → "Active" else → "Inactive"
Checks if is_verified == True → "Verified" else → "Unverified"

"""

raw_data = {
    "user_id"        : "1001",
    "account_balance": "5400.75",
    "is_verified"    : "True",
    "credit_score"   : "742",
    "transaction_ids": "TX001,TX002,TX003,TX004",
    "interest_rate"  : "3.5",
    "account_type"   : "  savings  ",
    "overdraft_limit": "-500",
}


raw_data = {
    "user_id"        : "1001",
    "account_balance": "5400.75",
    "is_verified"    : "True",
    "credit_score"   : "742",
    "transaction_ids": "TX001,TX002,TX003,TX004",
    "interest_rate"  : "3.5",
    "account_type"   : "  savings  ",
    "overdraft_limit": "-500",
}


def sanitize_record(raw_data):
    clean_dictionary = dict()

    clean_dictionary["user_id"]         = int(raw_data["user_id"])
    clean_dictionary["account_balance"] = float(raw_data["account_balance"])
    clean_dictionary["is_verified"]     = raw_data["is_verified"] == "True"
    clean_dictionary["credit_score"]    = int(raw_data["credit_score"])
    clean_dictionary["transaction_ids"] = raw_data["transaction_ids"].split(",")
    clean_dictionary["interest_rate"]   = float(raw_data["interest_rate"])
    clean_dictionary["account_type"]    = raw_data["account_type"].strip().upper()
    clean_dictionary["overdraft_limit"] = int(raw_data["overdraft_limit"])

    return clean_dictionary


def verify_types(clean_data):
    print(f"\n{'KEY':<20} | {'VALUE':<35} | TYPE")
    print("-" * 70)
    for key, value in clean_data.items():
        print(f"{key:<20} -> {str(value):<34} | {type(value).__name__}")


def calculate_financials(clean_data):
    balance  = clean_data["account_balance"]
    i_rate   = clean_data["interest_rate"]
    credit   = clean_data["credit_score"]
    overdraft = clean_data["overdraft_limit"]

    monthly_interest = round(balance * (i_rate / 100) / 12, 2)
    max_withdrawal   = balance + abs(overdraft)
    risk_score       = round((credit / 850) * 100, 2)

    return monthly_interest, max_withdrawal, risk_score


def generate_report(clean_data, financials):

    monthly_interest, max_withdrawal, risk_score = financials

    if clean_data["credit_score"] >= 700:
        rating = "Excellent"
    elif clean_data["credit_score"] >= 600:
        rating = "Good"
    else:
        rating = "Poor"

    if clean_data["account_balance"] > 0:
        status = "Active"
    else:
        status = "Inactive"

    if clean_data["is_verified"]:
        verification = "Verified"
    else:
        verification = "Unverified"

    if clean_data["is_verified"] and clean_data["credit_score"] >= 700 and clean_data["account_balance"] > 5000:
        grade = "PLATINUM"
    elif clean_data["is_verified"] and clean_data["credit_score"] >= 600:
        grade = "GOLD"
    elif clean_data["is_verified"]:
        grade = "SILVER"
    else:
        grade = "BASIC"

    print(f"\n{'═' * 38}")
    print(f"{'VAULTCORE ACCOUNT REPORT':^38}")
    print(f"{'═' * 38}")

    print(f"\nUser ID           : {clean_data['user_id']}")
    print(f"Account Type      : {clean_data['account_type']}")
    print(f"Verification      : {verification}")
    print(f"Account Status    : {status}")
    print(f"Credit Rating     : {rating}")

    print(f"\nBalance           : ${clean_data['account_balance']}")
    print(f"Monthly Interest  : ${monthly_interest}")
    print(f"Max Withdrawal    : ${max_withdrawal}")
    print(f"Risk Score        : {risk_score}%")

    print(f"\nTransaction IDs   : {', '.join(clean_data['transaction_ids'])}")
    print(f"Total Transactions: {len(clean_data['transaction_ids'])}")

    print(f"\n{'═' * 40}")
    print(f"  VaultCore Security Grade : {grade}")
    print(f"{'═' * 40}")


print("═" * 40)
print("   VAULTCORE SYSTEM INITIALIZING...")
print("═" * 40)

print("\n--- RAW DATA RECEIVED ---")
print("--- SANITIZING & CONVERTING TYPES ---")

clean_data = sanitize_record(raw_data)
verify_types(clean_data)

print("\n--- CALCULATING FINANCIALS ---")

financials = calculate_financials(clean_data)
generate_report(clean_data, financials)



