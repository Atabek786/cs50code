import random


def main():
    level = get_level()
    solved = 0
    for i in range(10):
        problem = generate_integer(level)

        for j in range(3):
            print(problem['expression'])
            user_answer = get_user_answer()

            if user_answer == problem["solution"]:
                solved += 1
            else:
                    print("EEE")
        else:
            print(problem["solution"])
    print("Score: ", solved)

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
        problem = {
            "expression": f"{x} + {y} =",
            "solution": x + y
        }

        return problem

def get_user_answer():
    try:
        return int(input("Your answer: "))
    except ValueError:
        print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    main()