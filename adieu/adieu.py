import inflect

p = inflect.engine()

names = []

try:
    while True:
        name = input("Name: ")

        
except EOFError:
    pass

print(f"Adieu, adieu to {name}")
