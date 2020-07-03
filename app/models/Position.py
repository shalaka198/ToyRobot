from app.models.direction import Direction

class Position:

    def __init__(self, x_coordinate:int, y_coordinate:int, direction:Direction):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.direction = direction