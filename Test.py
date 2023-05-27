import unittest
from App import run_guess

class TestGuessGame(unittest.TestCase):
    def test_correct_guess(self):
        answer = 5
        result = run_guess(5, answer)
        self.assertTrue(result)

    def test_incorrect_guess(self):
        answer = 7
        result = run_guess(3, answer)
        self.assertFalse(result)

    def test_out_of_range_guess(self):
        answer = 2
        result = run_guess(12, answer)
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()