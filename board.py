import random

from direction import Direction
from location import Location
from rejectReason import IllegalMove


class Board(object):

    @staticmethod
    def initial_board_generator():
        board = Board.get_winning_board()
        empty_cell_location = Board.find_empty_cell(board)
        transformations = random.randrange(100, 150)
        for i in range(transformations):
            move = random.choice(list(Board.get_legal_moves(empty_cell_location)))
            Board.make_a_move(board, empty_cell_location, move)
        return board

    @staticmethod
    def get_winning_board():
        return [[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12],
                [13, 14, 15, ""]]

    @staticmethod
    def get_legal_moves(empty_cell_location):
        n = 4
        maximum_index = n - 1
        minimum_index = 0
        legal_moves = set()
        if empty_cell_location.row > minimum_index:
            legal_moves.add(Direction.DOWN)
        if empty_cell_location.row < maximum_index:
            legal_moves.add(Direction.UP)
        if empty_cell_location.col > minimum_index:
            legal_moves.add(Direction.RIGHT)
        if empty_cell_location.col < maximum_index:
            legal_moves.add(Direction.LEFT)
        return legal_moves

    @staticmethod
    def is_move_legal(direction, empty_cell_location):
        return direction in Board.get_legal_moves(empty_cell_location)

    @staticmethod
    def make_a_move(board, empty_cell_location, direction):
        # type: (list, Location, Direction) -> None
        if direction not in Board.get_legal_moves(empty_cell_location):
            raise IllegalMove
        if direction == Direction.UP:
            delta_row, delta_col = 1, 0
        elif direction == Direction.DOWN:
            delta_row, delta_col = -1, 0
        elif direction == Direction.RIGHT:
            delta_row, delta_col = 0, -1
        else:  # direction == Direction.LEFT:
            delta_row, delta_col = 0, 1
        board[empty_cell_location.row][empty_cell_location.col], \
            board[empty_cell_location.row + delta_row][empty_cell_location.col + delta_col] = \
            board[empty_cell_location.row + delta_row][empty_cell_location.col + delta_col],\
            board[empty_cell_location.row][empty_cell_location.col]
        empty_cell_location.row += delta_row
        empty_cell_location.col += delta_col

    @staticmethod
    def find_empty_cell(board):
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == "":
                    return Location(row, col)
