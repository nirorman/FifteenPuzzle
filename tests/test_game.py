import unittest
from game import Game


class GameTestCase(unittest.TestCase):
    def setUp(self):
        self.game = Game([[1, 2, 3, 4],
                          [5, 6, 7, 8],
                          [9, 10, 11, 12],
                          [13, 14, 15, ""]])

    def get_char_func(self):
        if self.game.number_of_moves_taken == 0:
            return '\x1b[B'
        else:
            return 'q'

    def test_winning_scenario(self):
        self.game.play(self.get_char_func)

    def test_scenario(self):
        self.game.play(self.get_char_func)


if __name__ == '__main__':
    unittest.main()
