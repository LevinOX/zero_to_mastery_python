import unittest
import guessing_game
answer, guess = 5, 5
first, last = 1, 10


class TestMain(unittest.TestCase):
    def test_True(self):
        result = guessing_game.guess_fcn(answer, guess, first, last)
        self.assertTrue(result)

    def test_wrong_guess(self):
        result = guessing_game.guess_fcn(answer, 0, first, last)
        self.assertIsNone(result)

    def test_wrong_number(self):
        result = guessing_game.guess_fcn(answer, 11, first, last)
        self.assertIsNone(result)

    def test_wrong_type(self):
        result = guessing_game.guess_fcn(answer, 'string', first, last)
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
