from pyfiglet import Figlet
import sys
import random


prompt = input("Input: ")

if sys.argv == 0:
    converted = random(Figlet(prompt))
    print(converted)
elif sys.argv == 2:
    converted = Figlet(sys.argv[2])
    print(converted)
else:
    print("Type 0 or 2 command line arguments")
