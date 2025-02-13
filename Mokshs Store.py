print("Welcome to Mokshs Store!!")

items = {
    "mushroom": 2.50,
    "carrot": 1.00,
    "apple": 1.50,
    "banana": 0.75,
    "orange": 1.20,
    "bread": 2.00,
    "milk": 1.80
}

cart = {}

def show_items():
    print("\nItems for Sale:")
    for item, price in items.items():
        print(f"{item.capitalize()} - ${price:.2f}")

def add_to_cart(item, quantity):
    if item in items:
        if item in cart:
            cart[item] += quantity
        else:
            cart[item] = quantity
        print(f"Added {quantity} {item}(s) to your cart.")
    else:
        print("Item not found.")

def view_cart():
    print("\nYour Cart:")
    if not cart:
        print("Cart is empty.")
        return
    total = 0
    for item, quantity in cart.items():
        price = items[item] * quantity
        total += price
        print(f"{item.capitalize()} x{quantity} - ${price:.2f}")
    print(f"Total: ${total:.2f}")

def checkout():
    if not cart:
        print("Your cart is empty. Nothing to checkout.")
    else:
        view_cart()
        print("Thanks for shopping!")

# Example usage:
show_items()
add_to_cart("mushroom", 2)
add_to_cart("apple", 3)
add_to_cart("banana", 5)
view_cart()
checkout()
