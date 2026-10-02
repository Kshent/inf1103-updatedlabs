"""Inventory Management System - Phase 1

Products are stored as dictionaries inside a list.
"""

LINE = "-" * 48

# Each product is a dictionary; the inventory is a list of them.
inventory = [
    {"id": "P001", "name": "Laptop", "price": 1200.00, "stock": 15},
    {"id": "P002", "name": "Mouse", "price": 25.50, "stock": 40},
    {"id": "P003", "name": "Keyboard", "price": 45.00, "stock": 25},
]


def read_number(prompt, number_type):
    """Keep asking until the user enters a non-negative number of number_type."""
    while True:
        try:
            value = number_type(input(prompt))
            if value < 0:
                print("Value cannot be negative.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def generate_product_id(inventory):
    """Return the next sequential ID: P001, P002, P003, ..."""
    numbers = [int(p["id"][1:]) for p in inventory if p["id"][1:].isdigit()]
    next_number = max(numbers, default=0) + 1
    return f"P{next_number:03d}"


def add_product(inventory):
    """Prompt for product details and add a new product with an auto ID."""
    print("\nAdd New Product")
    product_id = generate_product_id(inventory)
    print(f"Product ID: {product_id}")

    inventory.append({
        "id": product_id,
        "name": input("Product Name: ").strip(),
        "price": read_number("Price: ", float),
        "stock": read_number("Stock Quantity: ", int),
    })
    print("Product added successfully!")


def display_all(inventory):
    """Print every product in the inventory."""
    print("\nCurrent Inventory")
    print(LINE)
    if not inventory:
        print("Inventory is empty.")
    for p in inventory:
        print(f"ID: {p['id']} | Name: {p['name']} | "
              f"Price: ${p['price']:.2f} | Stock: {p['stock']}")
    print(LINE)


def main():
    display_all(inventory)
    add_product(inventory)
    display_all(inventory)


if __name__ == "__main__":
    main()