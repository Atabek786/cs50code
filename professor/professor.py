import random


def main():
    level = get_level()
    solved = 0
    for i in range(10):
        problem = generate_integer(level)
        print(problem['expression'])
        for j in range(3):
            user_answer = get_user_answer()

            if user_answer == problem["solution"]:
                solved += 1
                break
            else:
                    print("EEE")
        if j == 2:
            print(problem["solution"])

    print("Score: ", solved)

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if 1 <= level <= 3:
                return level
            else:
                print("Select level between 1-3")
        except ValueError:
            print("Enter number")


def generate_integer(level):
    for i in range(10):
        if level == 1:
            x = random.randint(0,9)
            y = random.randint(0,9)
        elif level == 2:
            x = random.randint(10,99)
            y = random.randint(10,99)
        else:
            x = random.randint(100,999)
            y = random.randint(100,999)

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