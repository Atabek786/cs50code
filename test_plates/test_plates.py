from plates import is_valid

def main():
    test_length()
    test_number()
    test_lwrcase_and_uppcase()
    test_long()

def test_length():
    assert is_valid("C") == False
    assert is_valid("CS") == True
    assert is_valid("CS5") == True
    assert is_valid("CS50") == True

def test_number():
    assert is_valid("5") == False
    assert is_valid("50") == False
    assert is_valid("50C") == False
    assert is_valid("50CS") == False

def test_lwrcase_and_uppcase():
    assert is_valid("cS50") == True
    assert is_valid("Cs50") == True
    assert is_valid("cs50") == True
    assert is_valid("CS50") == True

def test_long():
    assert is_valid("cSx50") == False
    assert is_valid("ATA295") == False
    assert is_valid("139Ata") == False
    assert is_valid("A22bek") == False

if __name__ == "__main__":
    main()