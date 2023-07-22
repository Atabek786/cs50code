import random


def main():
    level = get_level()

    problem = generate_integer(level)

    print(problem)


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
        x = random.randint(1,9)
        y = random.randint(1,9)
        problem = x + y
        print(problem)

if __name__ == "__main__":
    main()