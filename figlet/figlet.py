
import pyfiglet
import sys







prompt = input("Enter a string: ")
prompt = pyfiglet.Figlet(prompt)
prompt.setFront(font=f)
print(pyfiglet.renderText(prompt))