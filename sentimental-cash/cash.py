def main():
    cents = float(input())


    quarters = calculate_quarters(cents)
    cents = cents - quraters * 25

    dimes = calculate_dimes(cents)
    cents = cents - dimes * 10

    nickels = calculate_nickels(cents)
    cents = cents - nickels * 5

    pennies = calculate_pennies(cents)
    cents = cents - pennies * 1

    coins = quarters + dimes + nickels + pennies

    print("Total number of coins given: " + coins)





def get_cents():
    while True:
        cents = int(input("Number of cents: "))
        if cents < 0:
            break
    return cents

def calculate_quarters(cents):
    quarters = 0
    while cents >= 25:
        cents = cents - 25
        quraters += 1
    return quarters

def calculate_dimes(cents):
    dimes = 0
    while cents >= 10:
        cents = cents - 10
        dimes += 1
    return dimes

def calculate_nickels(cents):
    nickels = 0
    while cents >= 5:
        cents = cents - 5
        nickels += 1
    return nickels

def calculate_pennies(cents):
    pennies = 0
    while cents >= 1:
        cents = cents - 1
        pennies += 1
    return pennies

main()

