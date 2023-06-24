import str
greeting = input("Greeting: ")
if greeting.isdigit():
    print("Print a string")
if greeting.isidentifier('hello'):
    print("$0")
elif greeting.isidentifier('h'):
    print("$20")
else:
    print("$100")

