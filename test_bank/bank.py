
def main():
    user_greeting = input("Enter your greeting: ").strip().lower()
    fee = value(user_greeting)
    print(f"Fee: ${fee}")


def value(greeting):  # Remove leading whitespace and convert to lowercase
    if greeting.startswith("hello"):
        return 0
    elif greeting.startswith("h"):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()