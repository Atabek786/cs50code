from um import count

def main():
    test_correct()
    test_incorrect()
    test_without()
    test_numbers()

def test_correct():
    assert count("Um, thanks for the album.") == 1
    assert count("Um, thanks, um...") == 2


def test_incorrect():
    assert count("Um, thanks for the zoo.") == 0
    assert count("Um, thanks, dum...") == 0

def test_without():
    assert count(" thanks for the album.") == 0
    assert count(" thanks...") == 0

def test_numbers():
    assert count("1, 2, 3, 4...") == 0
    assert count("I just got 100/100 in the test score!") == 0

if __name__ == "__main__":
    main()
