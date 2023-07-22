import random


def main():
    level = get_level()

    problem = generate_integer(level)

    print(problem)


def get_level():
    try:
        while True:
            level = int(input("Level: "))
            if level > 3 or level <= 0:
                pass
            else:
                return level
    except ValueError:
        print("Select level between 1-3")


def generate_integer(level):
    for i in range(10):
        x = random.randint(1,9)
        y = random.randint(1,9)
        problem = f"{x} + {y} ="
        return problem

if __name__ == "__main__":
    main()