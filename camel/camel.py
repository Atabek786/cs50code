from re import sub

def main():
    name = input("camelCase: ")

    converted = snake_case(name)

    print("snake_case: " + converted)

def snake_case(s):
    s = sub('([A-Z][a-z]+)', r'\1', s)
    s = sub('([A-Z]+)', r'_\1', s)
    s = sub('-', '_', s)
    return s.lower()

main()