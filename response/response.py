import re

def main():
    print(validation(input("What's your email address? ")))

def validation(s):
    email = validators.email(s)
    if ValueError:
        print("INVALID")
    else:
        print("Valid")

if __name__ == "__main__":
    main()