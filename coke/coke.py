price = 50

while price > 0:
    print("Amount Due: ", price)
    insert = int(input("Insert coin: "))
    if insert in [25, 10, 5]:
        price -= insert


changed_owed = abs(price)

print(price)
