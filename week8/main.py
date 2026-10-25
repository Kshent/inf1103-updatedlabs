"""
Inventory Management System (OOP version).

main.py: menu, user input, and file handling.
Classes: Product (product.py), Inventory (inventory.py).
"""

import json
import os

from product import Product
from inventory import Inventory

INVENTORY_FILE = "inventory2.json"
LINE = "-" * 48


# ------------------------------------------------------------- file handling
def load_inventory(inventory):
    """Fill the Inventory object from INVENTORY_FILE if it exists."""
    if not os.path.exists(INVENTORY_FILE):
        print(f"{INVENTORY_FILE} not found. Starting with an empty inventory.")
        return

    print(f"{INVENTORY_FILE} found.")
    try:
        with open(INVENTORY_FILE, "r") as file:
            for data in json.load(file):
                inventory.add_product(Product.from_dict(data))
        print("Inventory loaded successfully.")
    except (json.JSONDecodeError, OSError, KeyError, TypeError):
        print("Could not read the file. Starting with an empty inventory.")


def save_inventory(inventory):
    """Write the Inventory contents to INVENTORY_FILE."""
    try:
        with open(INVENTORY_FILE, "w") as file:
            json.dump(inventory.to_list(), file, indent=4)
        print(f"Inventory saved successfully to {INVENTORY_FILE}.")
    except OSError as error:
        print(f"Error saving inventory: {error}")


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


# ------------------------------------------------------------- menu actions
def add_product(inventory):
    print("\nAdd New Product")
    product_id = inventory.generate_product_id()
    print(f"Product ID: {product_id}")

    name = input("Product Name: ").strip()
    price = read_number("Price: ", float)
    stock = read_number("Stock Quantity: ", int)

    inventory.add_product(Product(product_id, name, price, stock))
    print("Product added successfully!")


def update_stock(inventory):
    print("\nUpdate Stock")
    product = inventory.search_product(input("Enter Product ID: ").strip())

    if product is None:
        print("Product not found.")
        return

    print("Product Found:")
    print(f"Name: {product.name}")
    print(f"Current Stock: {product.stock}")
    product.update_stock(read_number("New Stock Quantity: ", int))
    print("Stock updated successfully!")


def search_product(inventory):
    print("\nSearch Product")
    product = inventory.search_product(input("Enter Product ID: ").strip())

    if product is None:
        print("Product not found.")
        return

    print("Product Found")
    print(LINE)
    product.display_information()
    print(LINE)


# ------------------------------------------------------------------ menu/main
def show_menu():
    print("\n----------- MENU -----------")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")
    print("----------------------------")


def main():
    print("=" * 40)
    print("INVENTORY MANAGEMENT SYSTEM")
    print("=" * 40)

    inventory = Inventory()
    load_inventory(inventory)

    while True:
        show_menu()
        choice = input("Enter option: ").strip()

        if choice == "1":
            inventory.display_all()
        elif choice == "2":
            add_product(inventory)
        elif choice == "3":
            update_stock(inventory)
        elif choice == "4":
            search_product(inventory)
        elif choice == "5":
            print("Saving inventory...")
            save_inventory(inventory)
        elif choice == "6":
            print("Saving inventory before exit...")
            save_inventory(inventory)
            print("Thank you for using Inventory Management System.")
            print("Program terminated.")
            break
        else:
            print("Invalid option. Please choose 1-6.")


if __name__ == "__main__":
    main()