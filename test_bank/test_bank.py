from bank import value

def test_uppercase():
    assert value("HELLO, I WANT TO TAKE 100 BUCKS")


def test_lowercase():
    assert value("hello, i want to take 100 bucks")


def test_hey_uppcase():
    assert value("HEY, I WANT TO TAKE 100 BUCKS")


def test_hey_lwrcase():
    assert value("hey, i want to take 100 bucks")


def test_other():
    assert value("wassup, i want to take 100 bucks")