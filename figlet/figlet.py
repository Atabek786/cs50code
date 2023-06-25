import sys, random
from pyfiglet import Figlet

figlet = Figlet()


fonts = figlet.getFonts()

try:
    if len(sys.argv) == 1:
        user = input("Input: ")
        f = random.choice(Figlet.getFonts())
        Figlet.setFont(font = f)
        print(f"Output: {Figlet.renderText(user)}")
    elif sys.argv[1] == '-f' or sys.argv[1] == "--font":
        if sys.argv[1] == "-f" or sys.argv[1] == "--font":
            user = input("Input: ")
            fig = Figlet.setFont(font=sys.argv[2])
            print(f"Output: {Figlet.renderText(user)}")
        else:
            sys.exit("Invalid usage")
except:
    sys.exit("Invalid usage")