from um import count

def main():
    test_correct()
    test_incorrect()

def test_correct():
    assert count("Um, thanks for the album.") == 1
    assert count("Um, thanks, um...") == 2


def test_incorrect():
    assert count("Um, thanks for the album.") == 0
    assert count("Um, thanks, um...") == 0

if __name__ == "__main__":
    main()