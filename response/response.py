import re

def main():
    result = validation(input("What's your email address? "))
    if result:
        print("Valid")
    else:
        print("Invalid")

def validation(s):
    if re.search(r"^\w+@(\w+\.)?\w+\.edu$", s, re.IGNORECASE):
        return True
    else:
        return False

if __name__ == "__main__":
    main()
