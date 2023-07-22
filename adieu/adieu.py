import inflect

p = inflect.engine()

names = []

try:
    while True:
        name = input("Name: ")

        names.append(name)

except EOFError:
    pass

# Replace commas with "and" in each name
updated_names = [name.replace(',', ' and ') for name in names]

print(f"Adieu, adieu to {', '.join(updated_names)}")

