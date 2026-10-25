"""Inventory class: manages a collection of Product objects."""

LINE = "-" * 48


class Inventory:
    def __init__(self):
        self.__products = []

    def add_product(self, product):
        self.__products.append(product)

    def search_product(self, product_id):
        """Return the Product with the given ID (case-insensitive), or None."""
        for product in self.__products:
            if product.product_id.lower() == product_id.lower():
                return product
        return None

    def generate_product_id(self):
        """Return the next sequential ID: P001, P002, P003, ..."""
        numbers = [int(p.product_id[1:]) for p in self.__products
                   if p.product_id[1:].isdigit()]
        return f"P{max(numbers, default=0) + 1:03d}"

    def display_all(self):
        print("\nCurrent Inventory")
        print(LINE)
        if not self.__products:
            print("Inventory is empty.")
        for product in self.__products:
            product.display_information()
        print(LINE)

    def to_list(self):
        """Return products as a list of dictionaries (for saving)."""
        return [product.to_dict() for product in self.__products]