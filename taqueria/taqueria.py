def display_menu(menu):
    print("Menu:")
    for item, price in menu.items():
        print(f"{item}: ${price:.2f}")

def get_total_cost(items, menu):
    total = 0
    for item in items:
        if item.title() in menu:
            total += menu[item.title()]
    return total

# Menu dictionary
menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00,
}

print("Welcome to the Taqueria!")

# Display the menu
display_menu(menu)

# Initialize the list to store the user's ordered items
ordered_items = []

print("Enter the items you want to order (press Ctrl + D to finish):")
try:
    while True:
        item = input("Item: ")
        ordered_items.append(item)
        total_cost = get_total_cost(ordered_items, menu)
        print(f"Total: ${total_cost:.2f}")
except EOFError:
    print("\nOrder completed. Enjoy your meal!")
