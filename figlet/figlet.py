import sys, random
from pyfiglet import Figlet

figlet = Figlet()
if len(sys.argv) == 1:
    isRandomFont = True
elif len(sys.argv) == 3 and (sys.argv[1] == '-f' or sys.argv[1] == '--font'):
    isRandomFont = False
else:
    print("INVALID")
    sys.exit(1)

figlet.getFonts()

if isRandomFont == False:
    try:
        figlet.setFont(font=sys.argv[2])
    except:
        print("INVALID")
        sys.exit(1)
else:
    font = random.choice(figlet.getFonts())

msg = input("Input: ")


print("Output: ")
print(figlet.renderText(msg))