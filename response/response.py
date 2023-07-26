from validator_collection import validators

def main():
    result = validation(input("What's your email address?"))
    if result:
        print("Valid")
    else:
        print("Invalid")

def validation(s):
    if validators.is_email(s):
        return True
    else:
        return False

if __name__ == "__main__":
    main()