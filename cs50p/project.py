import art
import random

responses = ['Oookay, good luck doing that ! ', 'Good choice, bye!', 'Gotchaaa', 'Alright then!']


def main():
    while True:
        print(art.text2art("What do you wanna do today?", font="ogre", chr_ignore=True))
        option = options()


def options():
    try:
        n = input("P.S if you don't know what to do, press 1 so that I could help you :)")
        if n != '1' or n != 1:
            print(random(responses))
        else:
            options = int(input("Select a thing to do today: \n 1 studying \n 2 doing sports \n 3 reading books \n 4 "))



def function_2():
    ...


def function_n():
    ...


if __name__ == "__main__":
    main()