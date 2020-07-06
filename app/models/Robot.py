from app.models.direction import Direction
from app.models.board import Board

class Robot:

    def __init__(self, x_coordinate:int, y_coordinate:int, direction:Direction):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.direction = direction


    def place(self, x:int, y:int, direction:Direction):
        """
        Puts the robot on the table in position x,y and facing north, south, east or west direction
        x: x-coordinate on the board
        y: y-coordinate on the board
        direction: direction in which robot should face (valid values north, south, east or west)
        """
        self.x_coordinate = x
        self.y_coordinate = y
        self.direction = direction


    def move(self):
        """
        Moves the robot one unit forward in the direction it is currently facing
        """
        if self.robot_on_board():
            
            if self.direction == Direction.north and self.y_coordinate < Board.limit:
                self.y_coordinate += 1
            elif self.direction == Direction.south and self.y_coordinate > 0:
                self.y_coordinate -= 1
            elif self.direction==Direction.west and self.x_coordinate > 0:
                self.x_coordinate -= 1
            elif self.direction == Direction.east and self.x_coordinate < Board.limit:
                self.x_coordinate += 1


    def change_direction(self, move:str):
        """
        Rotates the robot 90 degrees in left/right direction without changing the x,y coordinate of the robot
        """
        if self.robot_on_board():            
            self.direction = Direction.direction_changes()[self.direction][move]

    
    def report(self):
        """
        Prints the coordinates(x,y) and direction of the robot
        """
        if self.robot_on_board():
            print('Robot is at ({},{}) facing {} direction'.format(self.x_coordinate, self.y_coordinate, self.direction.value))
            

    def robot_on_board(self):
        """
        Checks if robot is placed on the board
        """
        robot_placed = False
        if self.x_coordinate>-1 and self.y_coordinate>-1 and self.direction.value is not None:
            robot_placed = True
        else:
            #print("You haven't placed robot on the board yet!")
            #Ignore
            pass

        return robot_placed