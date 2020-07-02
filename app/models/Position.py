from app.models.Direction import Direction
from app.models.Coordinates import Coordinates

class Position:

    def __init__(self):
        self.coordinates = Coordinates(0,0)        
        self.direction = Direction.NORTH.value

    def set_position(self, x_coordinate, y_coordinate, direction):
        self.coordinates.x = x_coordinate
        self.coordinates.y = y_coordinate
        self.direction = direction