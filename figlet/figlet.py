
import pyfiglet
import sys

program = sys.argv[0]
arg1 = sys.argv[1]
arg2 = sys.argv[2]



prompt = input("Enter a string: ")
prompt = pyfiglet.Figlet(prompt)

print(pyfiglet.renderText(prompt))