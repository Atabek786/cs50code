import random


def main():
    ...


def get_level():
    try:
        while True:
            level = int(input("Level: "))
            if 3 < level or level <= 0:
                pass
            else:
                return level
    except ValueError:
        print("Select level between 1-3")
        pass


def generate_integer(level):
    for i in range(10):
        


if __name__ == "__main__":
    main()