price = 50

while price > 0:
    print("Amount Due :", price)
    insert = int(input("Insert coin: "))
    if insert in [25, 5, 10]:
        price -= insert

changed_owned = abs(price)

print("Changed owed: ",changed_owned)
