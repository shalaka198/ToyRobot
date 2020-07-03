from app.models.position import Position
from app.models.direction import Direction

class Robot:

    def __init__(self):
        # defaulting to coordinates 0,0 facing north direction
        self.position = Position(0,0,Direction.north)

    def place(self, x, y, direction):
        """
        Puts the robot on the table in position x,y and facing north, south, east or west direction

        x: x-coordinate on the board
        y: y-coordinate on the board
        direction: direction in which robot should face (valid values north, south, east or west)
        """
        pass

    def move(self):
        """
        Moves the robot one unit forward in the direction it is currently facing
        """
        pass

    def left(self):
        """
        Rotates the robot 90 degrees in left direction without changing the position of the robot
        """
        pass
    
    def right(self):
        """
        Rotates the robot 90 degrees in right direction without changing the position of the robot
        """
        pass
    
    def report(self):
        """
        Prints the coordinates(x,y) and direction of the robot
        """
        pass
    