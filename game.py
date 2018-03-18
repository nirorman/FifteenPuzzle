from board import Board
from direction import Direction
from users_move_enum import UsersMove
from printer import Printer


class Game(object):
    def __init__(self, initial_board):
        self.board = initial_board
        self.empty_cell_location = Board.find_empty_cell(initial_board)
        self.number_of_moves_taken = 0

    def play(self, read_input):
        Printer.print_start_game()
        while True:
            Printer.print_board(self.board)
            Printer.print_quiting_instructions()
            user_input_char = read_input()
            users_move = self.evaluate_users_move(user_input_char)
            is_game_finished = self.act_on_users_move(users_move, user_input_char)
            if is_game_finished:
                break

    def evaluate_users_move(self, user_input_char):
        if user_input_char == 'q':
            return UsersMove.ABORT_GAME
        elif Direction.is_arrow_key(user_input_char):
            direction = Direction.get_direction_from_key(user_input_char)
            if Board.is_move_legal(direction, self.empty_cell_location):
                return UsersMove.LEGAL_MOVE
            else:
                return UsersMove.ILLEGAL_MOVE
        else:
            return UsersMove.ILLEGAL_CHAR

    def act_on_users_move(self, users_move, user_input_char):
        # type: (UsersMove, str) -> bool
        is_game_finished = False
        if users_move == UsersMove.ABORT_GAME:
            Printer.print_game_aborted(self.number_of_moves_taken)
            is_game_finished = True
        elif users_move == UsersMove.ILLEGAL_MOVE:
            Printer.print_illegal_move()
        elif users_move == UsersMove.ILLEGAL_CHAR:
            Printer.print_illegal_char(user_input_char)
        elif users_move == UsersMove.LEGAL_MOVE:
            self._make_a_users_move(user_input_char)
            if self.board == Board.get_winning_board():
                Printer.print_board(self.board)
                Printer.print_winning_announcement(self.number_of_moves_taken)
                is_game_finished = True
        return is_game_finished

    def _make_a_users_move(self, user_input_char):
        direction = Direction.get_direction_from_key(user_input_char)
        Board.make_a_move(self.board, self.empty_cell_location, direction)
        self.number_of_moves_taken += 1
