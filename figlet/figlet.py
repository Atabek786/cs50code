import sys, random
from pyfiglet import Figlet

filget = Figlet()

user = input("Input: ")

fonts = Figlet.getFonts()

try:
    if len(sys.argv) == 1:
        f = random.choice(Figlet.getFonts())
        Figlet.setFont(font = f)
        print(f"Output: {Figlet.renderText(user)}")
    elif sys.argv[1] == '-f' or sys.argv[1] == "--font":
        if sys.argv[1] == "-f" or sys.argv[1] == 