from enum import Enum


class UsersMove(Enum):
    ABORT_GAME = 0
    ILLEGAL_MOVE = 1
    ILLEGAL_CHAR = 2
    LEGAL_MOVE = 3
