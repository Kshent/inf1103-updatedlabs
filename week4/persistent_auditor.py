import os

inventory = 0
failed_attempts = 0
total_units = 0
orders = []

INVENTORY_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "inventory.txt")
STARTING_ORDER_ID = 1001


def load_inventory():
    global inventory, orders
    try:
        with open(INVENTORY_FILE) as f:
            lines = f.read().splitlines()
    except FileNotFoundError:
        return

    if lines and lines[0].isdigit():
        inventory = int(lines[0])

    for line in lines[1:]:
        parts = line.split(",")
        if len(parts) == 3 and parts[0].isdigit() and parts[2].isdigit():
            orders.append((int(parts[0]), parts[1], int(parts[2])))


def save_inventory():
    with open(INVENTORY_FILE, "w") as f:
        f.write(f"{inventory}\n")
        for order_id, name, qty in orders:
            f.write(f"{order_id},{name},{qty}\n")


def get_valid_quantity(user_input):
    if user_input.isdigit():
        return int(user_input)
    print("Invalid input. Input positive number")
    return None


def calculate_tax(amount):
    return amount * 0.1


def get_next_order_id():
    return orders[-1][0] + 1 if orders else STARTING_ORDER_ID


def display_orders():
    print("Current Orders:")
    if not orders:
        print("(none yet)")
    for order_id, name, qty in orders:
        print(f"{order_id}, {name}, {qty}")



load_inventory()
display_orders()
print(f"Loaded starting inventory total: {inventory}")

while True:
    product_name = input("\nEnter Product Name (or 'quit' to exit): ")
    if product_name.lower() == "quit":
        break

    quantity = get_valid_quantity(input("Enter Quantity: "))
    if quantity is None:
        failed_attempts += 1
        continue

    order_id = get_next_order_id()
    orders.append((order_id, product_name, quantity))  # <-- history tracking
    inventory += quantity
    total_units += quantity

    print(f"\nNew Order Added:\n{order_id},{product_name}, {quantity}")
    print(f"Tax: {calculate_tax(quantity):.2f}. Current total inventory: {inventory}")
    print("(Not yet saved to file - orders list only lives in memory this run)")

print("\nFull history recorded this session:")
for order_id, name, qty in orders:
    print(f"  {order_id}, {name}, {qty}")
print(f"Total units entered this session: {total_units}")
print(f"Failed/Rejected entries: {failed_attempts}")