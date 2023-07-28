import art
import random

responses = ['Oookay, good luck doing that ! ', 'Good choice, bye!', 'Gotchaaa', 'Alright then!']

study_list = {
    'math': ['Algebra', 'Calculus', 'Geometry', 'Statistics'],
    'geography': ['Continents', 'Countries', 'Capital Cities', 'Physical Features'],
    'history': ['Ancient Civilizations', 'World Wars', 'Renaissance', 'Industrial Revolution'],
    'biology': ['Cell Biology', 'Genetics', 'Ecology', 'Anatomy'],
    'computer science': ['Programming', 'Data Structures', 'Algorithms', 'Web Development'],
}
book_list = {
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
    ],
}
sport_list = {
    'active sports': ['Baseball', 'Football', 'Soccer', 'Skiing', 'Boxing'],
    'passive sports': ['Camping', 'Hiking', 'Walking', 'Fishing', 'Swimming'],
}
game_list = {
    'action': ['Call of Duty', "Assassin's Creed", 'GTA V', 'Red Dead Redemption'],
    'adventure': ['The Legend of Zelda', 'Uncharted', 'Tomb Raider', 'God of War'],
    'puzzle': ['Portal', 'Candy Crush', 'Tetris', 'Portal 2'],
    'horror': ['Outlast', 'Outlast 2', 'Amnesia', 'Resident Evil 2', 'Silent Hill']
}
cook_list = {
    'italian': ['Pasta Carbonara', 'Margherita Pizza', 'Tiramisu', 'Lasagna'],
    'indian': ['Chicken Tikka Masala', 'Palak Paneer', 'Biryani', 'Gulab Jamun'],
    'mexican': ['Tacos', 'Enchiladas', 'Guacamole', 'Churros'],
    'turkish': ['Şiş Kebap', 'Döner', 'Köfte', 'Manti'],
    'arabic': ['Falafel', 'Baba ganoush', 'Hummus'],
}
def main():
    while True:
        print(art.text2art("What do you wanna do today?", font="ogre", chr_ignore=True))
        option = options()
        if option == 1:
            study()
        elif option == 2:
            sports()
        elif option == 3:
            books()
        elif option == 4:
            game()
        elif option == 5:
            cook()
        else:
            continue

def options():
    try:
        n = input("P.S if you don't know what to do, press 1 so that I could help you :)")
        if n != '1':
            print(random.choice(responses))
        else:
            options = int(input("Select an activity to do today: \n 1 study \n 2 sport \n 3 read \n 4 game \n 5 cook\n Answer: "))
            if options not in [1,2,3,4,5]:
                raise Exception()
            else:
                return options
    except (ValueError, Exception):
        print("Please don't prompt weird symbols :(")

def study():


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