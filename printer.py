import texttable as tt


class Printer(object):
    @staticmethod
    def print_board(board):
        tab = tt.Texttable()
        tab.add_rows(board, header=False)
        tab.set_cols_align(['c', 'c', 'c', 'c'])
        print tab.draw()

    @staticmethod
    def print_illegal_move():
        print("Sorry, that move is illegal in the current board state.")

    @staticmethod
    def print_illegal_char(user_input_char):
        printable = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
        print('Invalid input :(')
        print(
            'You pressed: "' + ''.join(
                ['\\' + hex(ord(i))[1:] if i not in printable else i for i in user_input_char]) + '"')
        print("Sorry, please press an arrow key. to exit press 'q'.")

    @staticmethod
    def print_start_game():
        print("************************************ Welcome to fifteen puzzle! ************************************\n"
              "- A tile can be moved to a neighbour empty place.\n"
              "- Use the arrow keys in your keyboard to move the tiles: \n"
              "     - left\n"
              "     - right\n"
              "     - up\n"
              "     - down \n"
              "- Use the 'q' key to quit the game.\n"
              "- Your number of moves is counted so think through your every move!\n"
              "- To win the game you need to order tiles from 1 to 15, \n"
              "  where tile number 1 is at the top left corner and empty one is at the bottom right corner\n"
              "********************************************* Good Luck! *******************************************\n")

    @staticmethod
    def print_winning_announcement(number_of_moves_taken):
        print("Great job! you won! Number of moves taken: {}".format(number_of_moves_taken))

    @staticmethod
    def print_game_aborted(number_of_moves_taken):
        print("Aborting game - Sorry to see you go, come back to try again! Number of moves taken = {}".format(number_of_moves_taken))

    @staticmethod
    def print_quiting_instructions():
        print("press 'q' to exit the game")
