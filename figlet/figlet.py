from pyfiglet import Figlet
import pyfiglet
import sys

program = sys.argv[0]
arg1 = sys.argv[1]
arg2 = sys.argv[2]

if arg1 == '-f' or arg1 == '--font':
    return Success
else:
    return


prompt = input("Enter a string: ")
prompt = Figlet()

print(pyfiglet.renderText(prompt))