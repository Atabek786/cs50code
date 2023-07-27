from project import hello, h, other

def main():
    ...

def test_hello():
    assert hello("Hello my name is") == 0

def test_h():
    assert h("Hi my name is") == 20

def test_other():
    assert other("What's going on?") == 100
