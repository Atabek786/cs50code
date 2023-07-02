
while True:
    cents = float(input("Enter the amount in cents: ").strip())
    if cents >= 0:
        break

cents = round(cents*100)

count = 0

while cents >= 25:
    cents = cents - 25
    count += 1



while cents >= 10:
    cents = cents - 10
    count += 1



while cents >= 5:
    cents = cents - 5
    count += 1



while cents >= 1:
    cents = cents - 1
    count += 1



print("Total number of coins given: " + str(count))

