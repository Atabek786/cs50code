from fuel import convert, gauge

def main():
    test_zero()
    test_punctuation()
    test_trues()
    test_letters()

def test_zero():
    assert convert("1/2") == "50%"










if __name__ == "__main__":
    main()