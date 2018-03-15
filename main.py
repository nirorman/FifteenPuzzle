#!/usr/bin/env python
from board import Board
from game import Game
import click


def main():
    initial_board = Board.initial_board_generator()
    game = Game(initial_board)
    game.play(read_input=click.getchar)

if __name__ == '__main__':
    main()
