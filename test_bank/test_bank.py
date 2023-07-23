from bank import value

def test_uppercase():
    assert value("HELLO, I WANT TO TAKE 100 BUCKS") == "Fee: $0"


def test_lowercase():
    assert value("hello, i want to take 100 bucks") == "Fee: $0"


def test_hey_uppcase():
    assert value("HEY, I WANT TO TAKE 100 BUCKS") == "Fee: $20"


def test_hey_lwrcase():
    assert value("hey, i want to take 100 bucks") == "Fee: $20"


def test_other():
    assert value("wassup, i want to take 100 bucks") == "Fee: $100"