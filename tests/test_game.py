import unittest

from direction import Direction
from game import Game
from rejectReason import IllegalMove
from users_move_enum import UsersMove


class GameTestCase(unittest.TestCase):
    def setUp(self):
        self.game = Game([[1, 2, 3, 4],
                          [5, 6, 7, 8],
                          [9, 10, 11, 12],
                          [13, 14, 15, ""]])

    def test_number_of_steps_taken(self):
        self.game = Game([[1, 2, 3, 4],
                          [5, 6, 7, 8],
                          [9, 10, 11, ""],
                          [13, 14, 15, 12]])
        self.game.play(lambda: Direction.UP)
        self.assertEquals(self.game.number_of_moves_taken, 1)

    def test_number_of_steps_taken_in_quit(self):
        self.game = Game([[1, 2, 3, 4],
                          [5, 6, 7, 8],
                          [9, 10, "", 11],
                          [13, 14, 15, 12]])
        self.game.play(lambda: 'q')
        self.assertEquals(self.game.number_of_moves_taken, 0)

    def test_act_on_users_move_abort(self):
        self.assertTrue(self.game.act_on_users_move(UsersMove.ABORT_GAME, 'q'))

    def test_act_on_users_move_game_won(self):
        self.game = Game([[1, 2, 3, 4],
                          [5, 6, 7, 8],
                          [9, 10, 11, ""],
                          [13, 14, 15, 12]])
        self.assertTrue(self.game.act_on_users_move(UsersMove.LEGAL_MOVE, str(Direction.UP)))

    def test_act_on_users_move_game_not_won(self):
        self.game = Game([[1, 2, 3, 4],
                          [5, 6, 7, 8],
                          [9, 10, 11, ""],
                          [13, 14, 15, 12]])
        self.assertFalse(self.game.act_on_users_move(UsersMove.LEGAL_MOVE, str(Direction.LEFT)))

    def test_act_on_users_move_game_exception(self):
        self.game = Game([[1, 2, 3, 4],
                          [5, 6, 7, 8],
                          [9, 10, 11, ""],
                          [13, 14, 15, 12]])
        with self.assertRaises(IllegalMove):
            self.assertFalse(self.game.act_on_users_move(UsersMove.LEGAL_MOVE,  str(Direction.RIGHT)))

    def test_evaluate_users_move_abort(self):
        self.assertEquals(self.game.evaluate_users_move('q'), UsersMove.ABORT_GAME)

    def test_evaluate_users_move_illegal_char(self):
        self.assertEquals(self.game.evaluate_users_move("p"), UsersMove.ILLEGAL_CHAR)

    def test_evaluate_users_move_illegal_move(self):
        self.assertEquals(self.game.evaluate_users_move(str(Direction.UP)), UsersMove.ILLEGAL_MOVE)

    def test_evaluate_users_move_legal_move(self):
        self.assertEquals(self.game.evaluate_users_move(str(Direction.DOWN)), UsersMove.LEGAL_MOVE)


if __name__ == '__main__':
    unittest.main()
