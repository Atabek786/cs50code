import random

def get_integer_input(prompt):
    while True:
        user_input = input(prompt)
        if user_input.isdigit():
            return int(user_input)
        else:
            print("Invalid input! Please enter a numeric value.")

randomizer = random.randint(1, 9)


try:
    while True:
        guess = get_integer_input("Guess: ")
        if guess > randomizer:
            print("Too large!")
        elif guess < randomizer:
            print("Too small!")
        elif guess == randomizer:
            print("Just right!")
            break
except ValueError:
    pass

