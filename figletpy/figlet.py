from pyfiglet import Figlet
import sys
import random

prompt = input("Input: ")

if len(sys.argv) == 1 :
    f = Figlet()
    availablefonts = f.getFonts()
    selectfont = random.choice(availablefonts)

    f = Figlet(font=selectfont)
    converted = f.renderText(prompt)
    print(converted)

elif len(sys.argv) == 2 :
    f = Figlet(font=sys.argv[1])
    converted = f.renderText(prompt)

    print(converted)
else:
    print("Type 0 or 2 command line arguments")
