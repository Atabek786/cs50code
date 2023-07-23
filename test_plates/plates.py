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
    elif number_check(s) == False:
        return False
    elif zero_check(s) == False:
        return False
    elif contains_punctuation(s) == True:
        return False
    elif doesnt_begin_with_letters(s) == True:
        return False
    else:
        return True


def number_check(n):
    firstnum = None
    for c in n:
        if c.isdigit():
            firstnum = c
            break
    if firstnum == None:
        return True
    if int(firstnum) == 0:
        return False
    index = n.index(firstnum)
    position = len(n) - index
    for c in n[-position:]:
        if not c.isdigit():
            return False
    return True



def zero_check(z):
    i = 0
    while i < len(z):
        if z[i].isalpha()== False:
            if z[i] == "0":
                return False
            else:
                break
        i += 1

def doesnt_begin_with_letters(a):
    if a[0].isalpha() == False or a[1].isalpha() == False:
        return True



def contains_punctuation(x):
    for char in x:
        if char in punctuation:
            return True


if __name__ == "__main__":
    main()