class Location(object):
    def __init__(self, row, col):
        self.row = row
        self.col = col

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
