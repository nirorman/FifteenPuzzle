import unittest
from board import Board
from direction import Direction
from location import Location
from rejectReason import IllegalMove


class BoardTestCase(unittest.TestCase):

    def setUp(self):
        self.board = [[1, 2, 3, 4],
                      [5, 6, 7, 8],
                      [9, 10, 11, 12],
                      [13, 14, 15, ""]]
        self.empty_cell_location = Location(3, 3)

    def test_get_final_board(self):
        tested_board = Board.get_winning_board()
        self.assertListEqual(tested_board, [[1, 2, 3, 4],
                                            [5, 6, 7, 8],
                                            [9, 10, 11, 12],
                                            [13, 14, 15, ""]])

    def test_get_legal_moves_bottom_right_location(self):
        moves = Board.get_legal_moves(Location(3, 3))
        self.assertSetEqual(moves, {Direction.DOWN, Direction.RIGHT})

    def test_get_legal_moves_top_right_location(self):
        moves = Board.get_legal_moves(Location(0, 3))
        self.assertSetEqual(moves, {Direction.UP, Direction.RIGHT})

    def test_get_legal_moves_top_left_location(self):
        moves = Board.get_legal_moves(Location(0, 0))
        self.assertSetEqual(moves, {Direction.LEFT, Direction.UP})

    def test_get_legal_moves_bottom_left_location(self):
        moves = Board.get_legal_moves(Location(3, 0))
        self.assertSetEqual(moves, {Direction.LEFT, Direction.DOWN})

    def test_get_legal_moves_middle_location(self):
        moves = Board.get_legal_moves(Location(1, 1))
        self.assertSetEqual(moves, {Direction.LEFT, Direction.UP, Direction.DOWN, Direction.RIGHT})

    def test_is_legal_move_down_true(self):
        self.assertTrue(Board.is_move_legal(Direction.DOWN, Location(3, 3)))

    def test_is_legal_move_right_true(self):
        self.assertTrue(Board.is_move_legal(Direction.RIGHT, Location(3, 3)))

    def test_is_legal_move_up_false(self):
        self.assertFalse(Board.is_move_legal(Direction.UP, Location(3, 3)))

    def test_is_legal_move_left_false(self):
        self.assertFalse(Board.is_move_legal(Direction.LEFT, Location(3, 3)))

    def test_init_board(self):
        Board.initial_board_generator()

    def test_make_a_legal_move_down(self):
        Board.make_a_move(self.board, self.empty_cell_location, Direction.DOWN)
        self.assertListEqual(self.board, [[1, 2, 3, 4],
                                          [5, 6, 7, 8],
                                          [9, 10, 11, ""],
                                          [13, 14, 15, 12]])
        self.assertEqual(self.empty_cell_location.row, 2)
        self.assertEqual(self.empty_cell_location.col, 3)

    def test_make_a_legal_move_right(self):
        Board.make_a_move(self.board, self.empty_cell_location, Direction.RIGHT)
        self.assertListEqual(self.board, [[1, 2, 3, 4],
                                          [5, 6, 7, 8],
                                          [9, 10, 11, 12],
                                          [13, 14, "", 15]])
        self.assertEqual(self.empty_cell_location.row, 3)
        self.assertEqual(self.empty_cell_location.col, 2)

    def test_make_an_illegal_move_up(self):
        with self.assertRaises(IllegalMove):
            Board.make_a_move(self.board, Location(3, 3), Direction.UP)

    def test_make_an_illegal_move_left(self):
        with self.assertRaises(IllegalMove):
            Board.make_a_move(self.board, Location(3, 3), Direction.LEFT)

    def test_empty_cell(self):
        self.assertEquals(Board.find_empty_cell([[1, 2, 3, 4],
                                                 [5, 6, 7, 8],
                                                 [9, 10, 11, 12],
                                                 [13, 14, 15, ""]]), Location(3, 3))

if __name__ == '__main__':
    unittest.main()
