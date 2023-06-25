import sys
from pyfiglet import Figlet
if len(sys.argv) == 1:
    isRandomFont = True
elif len(sys.argv) == 3 and (sys.argv[1] == '-f' or sys.argv[1] == '--font'):
    isRandomFont = False
else:
    sys.exit(1)

msg = input("Input: ")




figlet.getFonts()

if isRandomFont == False:
    figlet.setFont(font=sys.argv[2])
    print(figlet.renderText(msg))