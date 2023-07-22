import inflect

p = inflect.engine()

names = []

try:
    while True:
        name = input("Name: ")
        names.append(name)
except EOFError:
    pass

# Create a grammatically correct farewell message using the inflect library
if len(names) == 1:
    farewell_message = f"Adieu, adieu to {names[0]}."
elif len(names) == 2:
    farewell_message = f"Adieu, adieu to {names[0]} and {names[1]}."
else:
    farewell_message = f"Adieu, adieu to {', '.join(names[:-1])}, and {names[-1]}."

print(farewell_message)
