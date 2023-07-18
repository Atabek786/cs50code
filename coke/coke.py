price = 50

while price > 0:
    print("Amount Due :", price)
    insert = int(input("Insert coin: "))
    if insert in [25, 10, 5]:
        price -= insert
    else:
        print("only 25, 10, 5 cents are accepted")


changed_owed = abs(price)

print("Changed owed: ",changed_owed)
