import unittest
from unittest import TestCase, mock
from unittest.mock import patch
from ...models.board import Board
from ...models.robot import Robot
from ...handlers.command_handler import CommandHandler
from io import StringIO

class TestUserInput(TestCase):

    def setUp(self):
        self.board = Board(5)
        self.robot = Robot(-1,-1,None)
        self.command_handler = CommandHandler(self.board, self.robot)


    def tearDown(self):
        pass


    # def run_test(self, user_instruction, expected_result):
    #     with patch('builtins.input', return_value=user_instruction), patch('sys.stdout', new=StringIO()) as fake_out:
    #         self.command_handler.handle_user_input()
    #         self.assertEqual(fake_out.getvalue(), expected_result)


    # def test_user_instruction_should_be_valid(self):
    #     """
    #     Given set of instructions 
    #     When user enters an invalid instruction
    #     Then print message on console alerting user
    #     """       
    #     #self.run_test('AAA\nEXIT\n', '')
    #     pass


    def test_place_command(self):
        # arrange
        commands = [            
            'PLACE ', 
            'PLACE', 
            'AAA 1,1,NORTH',             
            'PLACE -1,1,NORTH', 
            'PLACE 10,1,NORTH',
            'PLACE 1,-1,NORTH',
            'PLACE 1,10,NORTH',
            'PLACE 1,1,AAA',
            'PLACE 1;1;NORTH'
            ]
        limit = self.board.dimension-1
        expected = (False,None,None,None)

        # act and assert
        for command in commands:            
            self.assertTupleEqual(self.command_handler.validate_place_command(command, limit), expected)