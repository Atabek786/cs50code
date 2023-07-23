
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    punctuation = {
    " ","!","#","$","%","&",
    "(",")","*","+",",","-",
    ".","/",":",";","<","=",
    ">","?","@","[","^","]",
    "^","_","`","{",",","|","}","~",
}
    s = s.strip().upper()

    if len(s) < 2 or len(s) > 6:
        return False

    if not s[0].isalpha() or not s[1].isalpha():
        return False

    if any(char.isdigit() for char in s):
        first_digit = next(char for char in s if char.isdigit())
        if first_digit == "0":
            return False

    if any(char in punctuation for char in s):
        return False

    return True


if __name__ == "__main__":
    main()
