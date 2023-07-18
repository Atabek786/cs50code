price = 50
while price > 0:
    print("Amount Due: ", price)
    insert = int(input("Insert coin: "))
    if insert == 25 or insert == 10 or insert == 5:
        new_price = price - insert
        print("Insert coin: ", new_price)
    else:
        print("only 25, 10, 5 cents accepted")

