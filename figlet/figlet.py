from pyfiglet import Figlet
import pyfiglet
import sys



prompt = input("Enter a string: ")
prompt = Figlet()
print(pyfiglet.renderText(prompt))