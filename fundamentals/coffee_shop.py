"""
You need to build a terminal-based Point of Sale (POS) system for a coffee shop.
The program should:Show a Menu: Display at least four drinks with their prices.
Take an Order: Ask the user which drink they want and how many.Handle Errors:
Alert the user if they pick something not on the menu.Calculate Costs:
Add a 5% tax to the subtotal.Print a Receipt: Show a clearly formatted final bill.

"""


def run_coffee_shop():
    menu = {
        "Espresso": 3.00,
        "Latte": 4.50,
        "Cappuccino": 4.00,
        "Mocha": 5.00
    }

    print("--- Welcome to Python Brew! ---")
    for item, price in menu.items():
        print(f"{item}: ${price:.2f}")
    choice = input("\nWhat would you like to order? ").capitalize()

    if choice in menu:
        try:
            quantity = int(input(f"How many {choice}s would you like? "))
            subtotal = menu[choice] * quantity
            tax = subtotal * 0.05
            total = subtotal + tax

            print("\n" + "=" * 20)
            print(f"   YOUR RECEIPT")
            print("=" * 20)
            print(f"Item:     {choice} (x{quantity})")
            print(f"Subtotal: ${subtotal:.2f}")
            print(f"Tax (5%): ${tax:.2f}")
            print(f"TOTAL:    ${total:.2f}")
            print("=" * 20)
            print("Enjoy your coffee!")

        except ValueError:
            print("Error: Please enter a whole number for quantity.")
    else:
        print("Sorry, that item is not on our menu today.")


run_coffee_shop()
