from enum import Enum


class Direction(Enum):
    UP = '\x1b[A'
    DOWN = '\x1b[B'
    LEFT = '\x1b[C'
    RIGHT = '\x1b[D'

    @staticmethod
    def get_key_direction_map():
        return {'\x1b[A': Direction.UP,
                '\x1b[B': Direction.DOWN,
                '\x1b[C': Direction.RIGHT,
                '\x1b[D': Direction.LEFT}

    @staticmethod
    def get_direction_from_key(arrow_key):
        return Direction.get_key_direction_map()[arrow_key]

    @staticmethod
    def is_arrow_key(key):
        return key in Direction.get_key_direction_map()
