def calculate_fee(greeting):
    greeting = greeting.lstrip().lower()  # Remove leading whitespace and convert to lowercase

    if greeting.startswith("hello"):
        return "$0"
    elif greeting.startswith("h"):
        return "$20"
    else:
        return "$100"

user_greeting = input("Enter your greeting: ")
fee = calculate_fee(user_greeting)
print("Fee:", fee)