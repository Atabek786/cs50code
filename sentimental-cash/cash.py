
def main():
    while True:
        try:
            cents = float(input("Enter the amount in cents: ").strip())
            if cents >= 0:
                break
            else:
                print("Invalid input. Amount must be non-negative.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    quarters = calculate_quarters(cents)
    cents = cents - quarters * 25

    dimes = calculate_dimes(cents)
    cents = cents - dimes * 10

    nickels = calculate_nickels(cents)
    cents = cents - nickels * 5

    pennies = calculate_pennies(cents)
    cents = cents - pennies * 1

    coins = quarters + dimes + nickels + pennies

    print("Total number of coins given: " + str(coins))




def calculate_quarters(cents):
    quarters = 0
    while True:
        try:
            cents = cents - 25
            if cents < 25:
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    return quarters

def calculate_dimes(cents):
    dimes = 0
    while True:
        try:
            cents = cents - 10
            if cents < 10:
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    return dimes

def calculate_nickels(cents):
    nickels = 0
    while True:
        try:
            cents = cents - 5
            if cents < 5:
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    return nickels

def calculate_pennies(cents):
    pennies = 0
    while True:
        try:
            cents = cents - 1
            if cents < 1:
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    return pennies

if __name__=="__main__":
    main()

