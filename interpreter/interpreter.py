import math

prompt = input("Expression: ")

x, y, z = prompt.split(" ")

x = float(x)
z = float(z)

if y == '+':
    result = x + z
elif y == '-':
    result = x - z
elif y == '*':
    result = x * z
elif y == '/':
    result = x / z
else:
    print("Invalid operator")

print(result)