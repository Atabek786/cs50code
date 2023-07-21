def prefix_ordered_items(order_history):
    # Create a dictionary to keep track of the number of times each item was ordered by each user
    user_item_count = {}

    # Loop through the order history to count the occurrences of each item for each user
    for order in order_history:
        item = order["item"]

        if item not in user_item_count:
            user_item_count[item] = 1
        else:
            user_item_count[item] += 1

    sorted_items = sorted(user_item_count.items(), key=lambda x: x[0].lower())
    # Generate the prefixed item names
    prefixed_items = []
    for item, count in sorted_items:

        # Add the prefixed item name to the list
        prefixed_item = f"{count} {item}"
        prefixed_items.append(prefixed_item)


    return prefixed_items

def get_order_from_user():
    order_history = []
    try:
        while True:
            item = input().strip()
            if not item:
                break
            order_history.append({"item": item})
    except EOFError:
        pass
    return order_history


# Get the order history from the user
order_history = get_order_from_user()

# Example usage
prefixed_items = prefix_ordered_items(order_history)
for item in prefixed_items:
    print(item.upper())

