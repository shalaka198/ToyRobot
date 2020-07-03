import unittest

class TestUserInput(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_user_instruction_should_be_valid(self):
        """
        Given set of instructions 
        When user enters an invalid instruction
        Then print message on console alerting user
        """
        pass

    def test_user_enters_invalid_move(self):
        """
        Given board dimension is 5 units by 5 units 
            and robot is at corner (4,0) facing EAST
        When enters invalid instruction MOVE
        Then do not move the robot to prevent it from falling 
            and print message on console alerting the user
        """
        pass