price = 50
print("Amount Due: ", price)
while price > 0:
    insert = int(input("Insert coin: "))
    if insert == 25 or insert == 10 or insert == 5:
        new_price = price - insert
        print("Amount due: ", new_price)
    else:
        print("only 25, 10, 5 cents accepted")


