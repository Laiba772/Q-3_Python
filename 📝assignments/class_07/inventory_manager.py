
# inventory_manager.py

class Product:
    def __init__(self, product_id, name, quantity, price):
        self.product_id = product_id
        self.name = name
        self.quantity = quantity
        self.price = price

    def __str__(self):
        return f"[{self.product_id}] {self.name} - Qty: {self.quantity}, Price: ${self.price:.2f}"


class Inventory:
    def __init__(self):
        self.products = {}

    def add_product(self, product):
        if product.product_id in self.products:
            print("❌ Product ID already exists!")
        else:
            self.products[product.product_id] = product
            print("✅ Product added successfully!")

    def view_inventory(self):
        if not self.products:
            print("🚫 Inventory is empty.")
        else:
            for product in self.products.values():
                print(product)

    def search_product(self, name):
        found = False
        for product in self.products.values():
            if name.lower() in product.name.lower():
                print(product)
                found = True
        if not found:
            print("🔍 Product not found.")

    def update_stock(self, product_id, quantity):
        if product_id in self.products:
            self.products[product_id].quantity = quantity
            print("✅ Stock updated.")
        else:
            print("❌ Product not found.")

    def delete_product(self, product_id):
        if product_id in self.products:
            del self.products[product_id]
            print("🗑️ Product deleted.")
        else:
            print("❌ Product not found.")


def main():
    inventory = Inventory()

    while True:
        print("\n📦 Inventory Management")
        print("1. Add Product")
        print("2. View Inventory")
        print("3. Search Product")
        print("4. Update Stock")
        print("5. Delete Product")
        print("6. Exit")

        choice = input("Enter choice (1-6): ")

        if choice == '1':
            pid = input("Enter Product ID: ")
            name = input("Enter Product Name: ")
            qty = int(input("Enter Quantity: "))
            price = float(input("Enter Price: "))
            product = Product(pid, name, qty, price)
            inventory.add_product(product)

        elif choice == '2':
            inventory.view_inventory()

        elif choice == '3':
            search_name = input("Enter name to search: ")
            inventory.search_product(search_name)

        elif choice == '4':
            pid = input("Enter Product ID: ")
            qty = int(input("Enter new quantity: "))
            inventory.update_stock(pid, qty)

        elif choice == '5':
            pid = input("Enter Product ID to delete: ")
            inventory.delete_product(pid)

        elif choice == '6':
            print("👋 Exiting... Thank you!")
            break

        else:
            print("❌ Invalid choice. Try again.")


if __name__ == "__main__":
    main()
