price = 50

while price > 0:
    print("Amount Due:", price)  # Adjusted the formatting of the print statement
    insert = int(input("Insert coin: "))
    if insert in [25, 5, 10]:
        price -= insert

change_owed = abs(price)  # Renamed 'changed_owned' to 'change_owed'

print("Change Owed:", change_owed)  # Adjusted the output message
