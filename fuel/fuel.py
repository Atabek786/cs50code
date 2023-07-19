def main():
    fuel = get_fraction("Fraction: ")
    print(f"{fuel}")


def get_fraction(prompt):
    while True:
        try:
            x = input(prompt)
            if x == '1/4':
                return "25%"
            elif x == '1/2':
                return "50%"
            elif x == '3/4':
                return "75%"
            elif x == '4/4':
                return "F"
            elif x == '0/4':
                return "E"
            else:
                print("Invalid input. Please enter a valid fraction (e.g., '1/4', '1/2', '3/4', '4/4', '0/4')")
        except ZeroDivisionError:
            pass
        except ValueError:
            pass


if __name__ == "__main__":
    main()
