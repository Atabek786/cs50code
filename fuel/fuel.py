def main():
    fraction = get_fraction("Enter the fraction (e.g., X/Y): ")
    percentage = calculate_percentage(fraction)

    if percentage <= 1:
        print("E")
    elif percentage >= 99:
        print("F")
    else:
        print(f"{percentage}%")

def get_fraction(prompt):
    while True:
        x = input(prompt)
        try:
            num, denom = x.split('/')
            num = int(num)
            denom = int(denom)

            if denom == 0:
                print("Invalid input. Denominator cannot be zero.")
            elif num > denom:
                print("Invalid input. Numerator cannot be greater than the denominator.")
            else:
                return num, denom
        except ValueError:
            print("Invalid input. Please enter a valid fraction (e.g., 'X/Y')")

def calculate_percentage(fraction):
    num, denom = fraction
    percentage = (num / denom) * 100
    return round(percentage)

if __name__ == "__main__":
    main()
