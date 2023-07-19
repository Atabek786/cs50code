
def main():
    fuel = get_str("Fraction: ")

    print(f"{fuel}")





def get_int(prompt):
    while True:
        try:
            x = int(input(prompt))
            if x == '1/4':
                print("25%")
            elif x == '1/2':
                print("50%")
            elif x== '3/4':
                print("75%")
            elif x == '4/4':
                print("F")
            elif x == '0/4':
                print("E")
        except ZeroDivisionError:
            pass
        except ValueError:
            pass


if __name__ == "__main__":
    main()