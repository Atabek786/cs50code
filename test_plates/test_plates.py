from plates import is_valid

def should_be_valid():
    assert is_valid("CS50") == True
    assert is_valid("ATA23") == True

def shouldnt_be_valid():
    assert is_valid("50CS") == False
    assert is_valid("23ATA") == False

def should_be_valid_reverse():
    assert is_valid("CS50") == False
    assert is_valid("ATA23") == False

def shouldnt_be_valid_reverse():
    assert is_valid("50CS") == True
    assert is_valid("23ATA") == True