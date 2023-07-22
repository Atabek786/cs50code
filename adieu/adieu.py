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

# Create a grammatically correct farewell message using the inflect library
farewell_message = f"Adieu, adieu to {p.join(updated_names)}."

print(farewell_message)
