import unittest
from unittest import TestCase, mock
from unittest.mock import patch
from ...models.board import Board
from ...models.robot import Robot
from ...models.direction import Direction
from ...handlers.command_handler import CommandHandler
from io import StringIO

class TestRobotMovements(unittest.TestCase):

    def setUp(self):
        self.board = Board(5)
        self.robot = Robot(-1,-1,None)
        self.command_handler = CommandHandler(self.board, self.robot)

    def tearDown(self):
        pass

    def test_place(self):
        # arrange
        x,y,direction = 2,2,Direction.east

        # act
        self.robot.place(x, y, direction)

        # assert
        self.assertEqual(self.robot.x_coordinate, x)
        self.assertEqual(self.robot.y_coordinate, y)
        self.assertEqual(self.robot.direction, direction)


    def test_move_happy_path(self):
        # arrange
        x,y,direction = 2,2,Direction.east
        self.robot.place(x, y, direction)

        # act
        self.robot.move()

        # assert
        self.assertEqual(self.robot.x_coordinate, x+1)
        self.assertEqual(self.robot.y_coordinate, y)
        self.assertEqual(self.robot.direction, direction)


    def test_move_unhappy_path(self):
        """
        @Scenario: Prevent robot from falling
        Given board dimension is 5 units by 5 units 
            and robot is at corner (4,0) facing EAST
        When enters instruction MOVE
        Then do not move the robot to prevent it from falling             
        """
        # arrange
        x,y,direction = 4,0,Direction.east
        self.robot.place(x, y, direction)        

        # act
        self.robot.move()

        # assert
        self.assertEqual(self.robot.x_coordinate, x)
        self.assertEqual(self.robot.y_coordinate, y)
        self.assertEqual(self.robot.direction, direction)


    def test_left(self):
        # arrange
        x,y,direction = 2,2,Direction.east
        self.robot.place(x, y, direction)

        # act
        self.robot.change_direction('left')

        # assert
        self.assertEqual(self.robot.x_coordinate, x)
        self.assertEqual(self.robot.y_coordinate, y)
        self.assertEqual(self.robot.direction, Direction.north)


    def test_right(self):
        # arrange
        x,y,direction = 2,2,Direction.east
        self.robot.place(x, y, direction)

        # act
        self.robot.change_direction('right')

        # assert
        self.assertEqual(self.robot.x_coordinate, x)
        self.assertEqual(self.robot.y_coordinate, y)
        self.assertEqual(self.robot.direction, Direction.south)


    def test_report(self):
        # arrange
        x,y,direction = 2,2,Direction.east
        self.robot.place(x, y, direction)

        # act and assert
        expected_result = f'Robot is at ({self.robot.x_coordinate},{self.robot.y_coordinate}) facing {self.robot.direction.value} direction\n'
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.robot.report()
            self.assertEqual(fake_out.getvalue(), expected_result)
        