import random

randomizer = random.randint(1, 9)

try:
    while True:
        prompt = int(input("Level: "))
        if prompt > randomizer:
            print("Too large")
            pass
        elif prompt < randomizer:
            print("Too small")
            pass
        elif prompt == randomizer:
            print("Just right")
        else:
            pass
except ValueError:
    pass
