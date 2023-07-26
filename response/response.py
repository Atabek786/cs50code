from validate_email import validate_email

def main():
    result = validation(input("What's your email address?"))
    if result:
        print("Valid")
    else:
        print("Invalid")

def validation(s):
    return validate_email(s)

if __name__ == "__main__":
    main()