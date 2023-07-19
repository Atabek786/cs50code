def get_int(prompt, item, total):
    while True:
        x = input(prompt)
        try:
            if x in menu:
                total += menu[x]  # Use x (user input) as the key to get the item's price from the menu dictionary
                return total
        except EOFError:
            return True  # If the input is interrupted (e.g., using Ctrl + D), return True to stop the loop
        except KeyError:
            print(f"Invalid item: {x}. Please enter a valid item from the menu.")

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

total = 0

# Get items from the user and update the total cost of the order
print("Enter the items you want to order (press Ctrl + D to finish):")
while True:
    result = get_int("Item: ", item, total)
    if result is True:
        break
    total = result

# Display the total cost of the order
print(f"Total: ${total:.2f}")
