import re

def main():
    print(validation(input("What's your email address? ")))

def validation(s):
    if re.search(r"^\w+@(\w+\.)?\w+\.edu$", s, re.IGNORECASE):
        print("Valid")
    else:
        print("Invalid")

if __name__ == "__main__":
    main()