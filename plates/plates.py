punctuation = {" ", "!", "#", "$", "%", "&", "(", ")", "*", "+", ",", "-", ".", "/", ":", ";", "<", "=", ">", "?", "@", "[", "^", "]", "^", "_", "`", "{", ",", "|", "}", "~"}

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) < 2:
        return False
    elif len(s) > 6:
        return False
    ...

def number_check(n):
    ...


def zero_check(z):
    ...

def doesnt_begin_with_letters(a):
    if a[0].isalpha() == False or a[1]



def contains_punctuation(x):
    for char in x:
        if char in punctuation:
            return True


main()