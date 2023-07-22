import random

randomizer = random.randint(1, 9)

try:
    while True:
        prompt = int(input("Level: "))
        if prompt.isdigit():
            if prompt > randomizer:
                print("Too large")
            elif prompt < randomizer:
                print("Too small")
            elif prompt == randomizer:
                print("Just right")
                break
        else:
            pass
except ValueError:
    pass

