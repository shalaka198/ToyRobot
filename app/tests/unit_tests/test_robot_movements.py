import unittest

class TestRobotMovements(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_place(self):
        """
        Given a board with dimension 5 units by 5 units 
        When user enters a PLACE instruction with valid x,y,direction
        Then robot position should be x,y,direction
        """
        pass

    def test_move(self):
        """
        Given a board with dimension 5 units by 5 units 
            and robot is at x,y,direction where it can move by 1 unit without falling
        When user enters a MOVE instruction
        Then robot position should be valid x,y,direction moved by 1 unit
        """
        pass

    def test_left(self):
        """
        Given a board with dimension 5 units by 5 units 
            and robot is at x,y,direction where it can move by 1 to left unit without falling
        When user enters a LEFT instruction
        Then robot position should be valid x,y,direction moved to left by 1 unit 
        """
        pass

    def test_right(self):
        """
        Given a board with dimension 5 units by 5 units 
            and robot is at x,y,direction where it can move by 1 to right unit without falling
        When user enters a RIGHT instruction
        Then robot position should be valid x,y,direction moved to right by 1 unit 
        """
        pass

    def test_report(self):
        """
        Given a board with dimension 5 units by 5 units 
            and robot is at valid x,y,direction
        When user enters a REPORT instruction
        Then print message on console informing user of the current robot position x,y,direction
        """
        pass