import inflect

p = inflect.engine()

names = []

try:
    while True:
        name = input("Name: ")

        names.append(name)

        updated = names.replace(',', ' and ')
except EOFError:
    pass

print(f"Adieu, adieu to {names}")
