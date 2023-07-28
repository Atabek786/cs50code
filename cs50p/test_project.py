import unittest
from unittest.mock import patch
from project import sports

class TestSports(unittest.TestCase):
    def test_sports_valid_choice(self):
        # Test case 1: Valid sport type choice
        user_input = "1\n"  # Simulate the user entering '1' followed by Enter

        # Patch the input function to return user_input
        with patch('builtins.input', side_effect=user_input):
            expected_output = "Enjoy your Active sports activities! Here are some options:\n- Baseball\n- Football\n- Soccer\n- Skiing\n- Boxing\n"
            self.assertEqual(sports(), expected_output)

if __name__ == "__main__":
    unittest.main()