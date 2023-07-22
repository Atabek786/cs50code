import random


def main():
    ...


def get_level():
    try:
        while True:
            levelprompt = int(input("Level: "))
            if 3 < levelprompt or levelprompt <= 0:
                pass
            else:
                return levelprompt
    except ValueError:
        print("Select level between 1-3")
        pass


def generate_integer(level):
    ...


if __name__ == "__main__":
    main()