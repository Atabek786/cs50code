from pyfiglet import Figlet
import figlet

prompt = input("Enter a string: ")
prompt = Figlet()
print(figlet.renderText(prompt))