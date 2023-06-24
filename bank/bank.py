
greeting = input("Greeting: ")
if greeting.isdigit():
    return False
if greeting.isidentifier('hello'):
    print("$0")
elif greeting.isidentifier('h'):
    print("$20")
else:
    print("$100")

