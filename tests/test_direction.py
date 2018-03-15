import unittest

from direction import Direction


class DirectionTestCase(unittest.TestCase):

    def test_is_arrow_key_up(self):
        self.assertTrue(Direction.is_arrow_key('\x1b[A'))

    def test_is_arrow_key_down(self):
        self.assertTrue(Direction.is_arrow_key('\x1b[B'))

    def test_is_arrow_key_right(self):
        self.assertTrue(Direction.is_arrow_key('\x1b[C'))

    def test_is_arrow_key_left(self):
        self.assertTrue(Direction.is_arrow_key('\x1b[D'))

    def test_is_not_arrow_key(self):
        self.assertFalse(Direction.is_arrow_key('d'))

if __name__ == '__main__':
    unittest.main()
