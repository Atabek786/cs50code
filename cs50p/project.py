import art
import random

responses = ['Oookay, good luck doing that ! ', 'Good choice, bye!', 'Gotchaaa', 'Alright then!']

books = {
    'horror': [
        'The Shining',
        'It',
        'Dracula',
        'Frankenstein',
        'Bird Box',
    ],
    'fantasy': [
        'The Hobbit',
        'Harry Potter and the Sorcerer\'s Stone',
        'The Name of the Wind',
        'Mistborn: The Final Empire',
        'The Way of Kings',
    ],
    'science fiction': [
        'The Blazing World and Other Writings by Margaret Cavendish (1666)',
        'Frankenstein by Mary Wollstonecraft Shelley',
        'The Time Machine by H.G. Wells (1895)',
        'The War of the Worlds by H.G. Wells (1897)',
    ],
    'romance': [
        'Pride and Prejudice, by Jane Austen (1813)',
        'Jane Eyre, by Charlotte Brontë (1847)',
        'Shanna, by Kathleen E. Woodiwiss (1977)',
        'Morning Glory, by Lavyrle Spencer (1993)',
        'The Viscount Who Loved Me, by Julia Quinn (2000)',
    ]
}
sports = {
    'soccer': ['5-a-side', '11-a-side', 'Futsal'],
    'basketball': ['3x3', '5x5'],
    'tennis': ['Singles', 'Doubles'],
    'running': []
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