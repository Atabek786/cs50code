from project import hello, h, other

def main():
    test_hello()
    test_h()
    test_other()

def test_hello():
    assert hello("Hello my name is") == None

def test_h():
    assert h("Hi my name is") == None

def test_other():
    assert other("What's going on?") == 100

if __name__ == "__main__":
    main()
