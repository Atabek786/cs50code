from validator_collection import validators

def main():
    email = input("What's your email address? ")
    try:

        email_address = validators.email(email)
        if email_address:
            print("Valid")
    except errors.EmptyValueError:
        print("Type your email!")
        pass
    except errors.InvalidEmailError:
        print("Invalid")
        pass

if __name__ == "__main__":
    main()
