from pyfiglet import Figlet
import sys
import random


prompt = input("Input: ")

if len(sys.argv) == 1 :
    converted = Figlet(font=random(prompt))

    converted = 
elif len(sys.argv) == 2 :
    converted = Figlet(font=sys.argv[2])
    print(converted)
else:
    print("Type 0 or 2 command line arguments")
