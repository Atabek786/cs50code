from validator_collection import validators

def main():
    result = validation(input("What's your email address? "))
    if result:
        print("Valid")
    else:
        print("Invalid")

def validation(s):
    return validators(s)

if __name__ == "__main__":
    main()
