class Board:

    limit = 0

    "A square board to place robot"
    def __init__(self, dimension):
        self.dimension = dimension
        Board.limit = dimension-1
