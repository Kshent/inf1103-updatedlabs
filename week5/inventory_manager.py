"""Inventory Management System - Phase 2

Products are stored as dictionaries inside a list.
The inventory is loaded from inventory.json when the file exists.
"""

import json
import os

INVENTORY_FILE = "inventory.json"
LINE = "-" * 48


# ---------------------------------------------------------------- persistence
def load_inventory():
    """Load inventory from INVENTORY_FILE if it exists; otherwise return []."""
    if not os.path.exists(INVENTORY_FILE):
        print(f"{INVENTORY_FILE} not found. Starting with an empty inventory.")
        return []

    print(f"{INVENTORY_FILE} found.")
    try:
        with open(INVENTORY_FILE, "r") as file:
            inventory = json.load(file)
        print("Inventory loaded successfully.")
        return inventory
    except (json.JSONDecodeError, OSError):
        print("Could not read the file. Starting with an empty inventory.")
        return []


# ------------------------------------------------------------- input helpers
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


# ---------------------------------------------------------- inventory actions
def find_product(inventory, product_id):
    """Return the product dictionary with the given ID, or None."""
    for product in inventory:
        if product["id"].lower() == product_id.lower():
            return product
    return None


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


def update_stock(inventory):
    """Change the stock quantity of an existing product."""
    print("\nUpdate Stock")
    product = find_product(inventory, input("Enter Product ID: ").strip())

    if product is None:
        print("Product not found.")
        return

    print("Product Found:")
    print(f"Name: {product['name']}")
    print(f"Current Stock: {product['stock']}")
    product["stock"] = read_number("New Stock Quantity: ", int)
    print("Stock updated successfully!")


def search_product(inventory):
    """Look up a product by ID and show its details."""
    print("\nSearch Product")
    product = find_product(inventory, input("Enter Product ID: ").strip())

    if product is None:
        print("Product not found.")
        return

    print("Product Found")
    print(LINE)
    print(f"ID: {product['id']}")
    print(f"Name: {product['name']}")
    print(f"Price: ${product['price']:.2f}")
    print(f"Stock: {product['stock']}")
    print(LINE)


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


# ------------------------------------------------------------------ menu/main
def show_menu():
    print("\n----------- MENU -----------")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Exit")
    print("----------------------------")


def main():
    print("=" * 40)
    print("INVENTORY MANAGEMENT SYSTEM")
    print("=" * 40)
    inventory = load_inventory()

    while True:
        show_menu()
        choice = input("Enter option: ").strip()

        if choice == "1":
            display_all(inventory)
        elif choice == "2":
            add_product(inventory)
        elif choice == "3":
            update_stock(inventory)
        elif choice == "4":
            search_product(inventory)
        elif choice == "5":
            print("Thank you for using Inventory Management System.")
            print("Program terminated.")
            break
        else:
            print("Invalid option. Please choose 1-5.")


if __name__ == "__main__":
    main()