def main():
    fuel = get_fraction("Fraction: ")
    print(fuel)


def get_fraction(prompt):
    valid_fractions = {
        '1/4': '25%',
        '1/2': '50%',
        '3/4': '75%',
        '4/4': 'F',
        '0/4': 'E',
    }

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
                fraction = f"{num}/{denom}"
                if fraction in valid_fractions:
                    return valid_fractions[fraction]
                else:
                    print("Invalid input. Please enter a valid fraction (e.g., '1/4', '1/2', '3/4', '4/4', '0/4')")
        except ValueError:
            print("Invalid input. Please enter a valid fraction (e.g., '1/4', '1/2', '3/4', '4/4', '0/4')")
        except ZeroDivisionError:
            print("Invalid input. Denominator cannot be zero.")


if __name__ == "__main__":
    main()
