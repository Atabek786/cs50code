from project import options, study, sports, books, game, cook

def test_options():
    # Test case 1: User selects an activity
    user_input = "1\n"  # Simulate the user entering '1' followed by Enter
    assert options(user_input) == 1

    # Test case 2: User doesn't know what to do
    user_input = "something\n"  # Simulate the user entering an invalid input
    assert options(user_input) == 1

def test_study():
    # Test case 1: Valid subject choice
    user_input = "1\n"  # Simulate the user entering '1' followed by Enter
    assert study(user_input) == "Great choice! Here are some topics in Math:\n- Algebra\n- Calculus\n- Geometry\n- Statistics\n"

    # Test case 2: Invalid subject choice
    user_input = "10\n"  # Simulate the user entering an invalid input
    assert study(user_input) == "Invalid choice. Please try again."

def test_sports():
    # Test case 1: Valid sport type choice
    user_input = "1\n"  # Simulate the user entering '1' followed by Enter
    assert sports(user_input) == "Enjoy your Active sports activities! Here are some options:\n- Baseball\n- Football\n- Soccer\n- Skiing\n- Boxing\n"

    # Test case 2: Invalid sport type choice
    user_input = "10\n"  # Simulate the user entering an invalid input
    assert sports(user_input) == "Invalid choice. Please try again."

# Add similar test functions for the remaining functions (books, game, cook)

# Run all the test functions
def run_tests():
    test_options()
    test_study()
    test_sports()
    # Call the remaining test functions here (books, game, cook)

if __name__ == "__main__":
    run_tests()
