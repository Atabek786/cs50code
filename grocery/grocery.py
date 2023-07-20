def prefix_ordered_items(order_history):
    # Create a dictionary to keep track of the number of times each item was ordered by each user
    user_item_count = {}

    # Loop through the order history to count the occurrences of each item for each user
    for order in order_history:
        item = order["item"]

        if item not in user_item_count[user]:
            user_item_count[user][item] = 1
        else:
            user_item_count[user][item] += 1

    # Generate the prefixed item names
    prefixed_items = []
    for order in order_history:
        item = order["item"]
        count = user_item_count[item]

        # Add the prefixed item name to the list
        prefixed_item = f"{item} ({count})"
        prefixed_items.append(prefixed_item)

    return prefixed_items

def get_order_from_user():
    order_history = []
    try:
        while True:
            item = input()
            order_history.append({"user": user, "item": item})
            return order_history
    except EOFError:
        return

# Get the order history from the user
order_history = get_order_from_user()

# Example usage
prefixed_items = prefix_ordered_items(order_history)
for item in prefixed_items:
    print(item)

