import unittest
from project import study, sports, books, game, cook

class TestProjectFunctions(unittest.TestCase):

    def test_study(self):
        # Test the study function
        # Write test cases and use assert methods to check if the output is as expected.
        self.assertEqual(study(), "Expected output for study function")

    def test_sports(self):
        # Test the sports function
        # Write test cases and assert statements as needed
        self.assertEqual(sports(), "Expected output for sports function")

    def test_books(self):
        # Test the books function
        # Write test cases and assert statements as needed
        self.assertEqual(books(), "Expected output for books function")

    def test_game(self):
        # Test the game function
        # Write test cases and assert statements as needed
        self.assertEqual(game(), "Expected output for game function")

    def test_cook(self):
        # Test the cook function
        # Write test cases and assert statements as needed
        self.assertEqual(cook(), "Expected output for cook function")

if __name__ == '__main__':
    unittest.main()
