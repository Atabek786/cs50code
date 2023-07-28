import art
import random

responses = ['Oookay, good luck doing that ! ', 'Good choice, bye!', 'Gotchaaa', 'Alright then!']

studying = {
    
}


def main():
    while True:
        print(art.text2art("What do you wanna do today?", font="ogre", chr_ignore=True))
        option = options()
        if option == 1:
            ...
        elif option == 2:
            ...
        elif option == 3:
            ...
        elif option == 4:
            ...
        elif option == 5:
            ...
        else:
            continue

def options():
    try:
        n = input("P.S if you don't know what to do, press 1 so that I could help you :)")
        if n != '1' or n != 1:
            print(random(responses))
        else:
            options = int(input("Select an activity to do today: \n 1 study \n 2 sports \n 3 books \n 4 game \n 5 cook\n Answer: "))
            if options not in [1,2,3,4,5]:
                raise Exception()
            else:
                return options
    except (ValueError, Exception):
        print("Please don't prompt weird symbols :(")

def study():
    ...

def sports():
    ...

def books():
    ...

def game():
    ...

def cook():
    ...



if __name__ == "__main__":
    main()