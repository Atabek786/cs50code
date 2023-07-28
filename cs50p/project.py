import art
import random

responses = ['Oookay, good luck doing that ! ', 'Good choice, bye!', 'Gotchaaa', '']


def main():
    while True:
        print(art.text2art("What do you wanna do today?", font="ogre", chr_ignore=True))
        option = options()


def options():
    try:
        n = input("P.S if you don't know what to do, press 1")
        if n != '1' or n != 1:
            print("Oookay, good luck doing that")



def function_2():
    ...


def function_n():
    ...


if __name__ == "__main__":
    main()