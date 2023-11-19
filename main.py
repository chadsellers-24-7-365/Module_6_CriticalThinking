# Module 6: Portfolio Milestone
# Steps - 4, 5, and 6
class ItemToPurchase:
    def __init__(self, item_name="none", item_description="none", item_price=0.0, item_quantity=0):
        self.item_name = item_name
        self.item_description = item_description
        self.item_price = item_price
        self.item_quantity = item_quantity


class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self, item_to_purchase):
        self.cart_items.append(item_to_purchase)

    def remove_item(self, item_name):
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                return
        print("Item not found in cart. Nothing removed.")

    def modify_item(self, item_to_purchase):
        for item in self.cart_items:
            if item.item_name == item_to_purchase.item_name:
                if item_to_purchase.item_description != "none":
                    item.item_description = item_to_purchase.item_description
                if item_to_purchase.item_price != 0:
                    item.item_price = item_to_purchase.item_price
                if item_to_purchase.item_quantity != 0:
                    item.item_quantity = item_to_purchase.item_quantity
                return
        print("Item not found in cart. Nothing modified.")

    def get_num_items_in_cart(self):
        total_quantity = sum(item.item_quantity for item in self.cart_items)
        return total_quantity

    def get_cost_of_cart(self):
        total_cost = sum(item.item_price * item.item_quantity for item in self.cart_items)
        return total_cost

    def print_total(self):
        if not self.cart_items:
            print("SHOPPING CART IS EMPTY")
            return

        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print(f"Number of Items: {self.get_num_items_in_cart()}")

        for item in self.cart_items:
            print(f"{item.item_name} @ ${item.item_price} = ${item.item_price * item.item_quantity}")

        total_cost = self.get_cost_of_cart()
        print(f"Total: ${total_cost:.2f}")

    def print_descriptions(self):
        if not self.cart_items:
            print("SHOPPING CART IS EMPTY")
            return

        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("Item Descriptions:")
        for item in self.cart_items:
            print(f"{item.item_name}: {item.item_description}")


def print_menu():
    print("\nMENU")
    print("a - Add item to cart")
    print("r - Remove item from cart")
    print("m - Modify item in cart")
    print("i - Output items' descriptions")
    print("o - Output shopping cart")
    print("q - Quit")


def main():
    # Example usage
    item1 = ItemToPurchase("Nike Romaleos", "Volt color, Weightlifting shoes", 189, 2)
    item2 = ItemToPurchase("Chocolate Chips", "Semi-sweet", 3, 5)
    item3 = ItemToPurchase("Powerbeats 2 Headphones", "Bluetooth headphones", 128, 1)

    cart = ShoppingCart("John Doe", "February 1, 2020")

    cart.add_item(item1)
    cart.add_item(item2)
    cart.add_item(item3)

    choice = None

    while choice != 'q':
        print_menu()
        choice = input("Choose an option: ")

        if choice == 'a':
            # Add item to cart
            item_name = input("Enter the item name: ")
            item_description = input("Enter the item description: ")
            item_price = float(input("Enter the item price: "))
            item_quantity = int(input("Enter the item quantity: "))
            new_item = ItemToPurchase(item_name, item_description, item_price, item_quantity)
            cart.add_item(new_item)

        elif choice == 'r':
            # Remove item from cart
            item_name = input("Enter the item name to remove: ")
            cart.remove_item(item_name)

        elif choice == 'm':
            # Modify item in cart
            item_name = input("Enter the item name to modify: ")
            item_description = input("Enter the new item description (press Enter to keep current): ")
            item_price = float(input("Enter the new item price (press Enter to keep current): ") or 0)
            item_quantity = int(input("Enter the new item quantity (press Enter to keep current): ") or 0)
            modified_item = ItemToPurchase(item_name, item_description, item_price, item_quantity)
            cart.modify_item(modified_item)

        elif choice == 'i':
            # Output items' descriptions
            cart.print_descriptions()

        elif choice == 'o':
            # Output shopping cart
            cart.print_total()

        elif choice == 'q':
            # Quit
            print("Exiting the program.")
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
