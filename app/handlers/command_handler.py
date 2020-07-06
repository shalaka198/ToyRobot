import logging
from app.models.board import Board
from app.models.robot import Robot
from app.models.direction import Direction

class CommandHandler:

    def __init__(self, board:Board, robot:Robot):
        self.board = board
        self.robot = robot

    def handle_user_input(self):
        exit = False
        while(not exit):        
            print("*******************************************************************************")
            print("Please enter one of the following valid instruction")
            print("1.'PLACE X,Y,F': Places robot at x,y location on the board facing one of north, south, east or west direction")
            print("Valid values for X and Y are between 0 and {}".format(Board.limit))
            print("F can have one of these values: {}".format(Direction.get_values()))
            print("2.'MOVE': Moves robot 1 unit forward in the direction it is facing")
            print("3.'LEFT': Rotates the robot 90 degrees in the left direction")
            print("4.'RIGHT': Rotates the robot 90 degrees in the right direction")
            print("5.'REPORT': Prints robot location (x,y) and direction in which it is facing")
            print("6.'EXIT': Exits the App")
            print("-------------------------------------------------------------------------------")

            command = input("What's your instruction:").strip().upper()
            try:
                if command.startswith('PLACE'):
                    logging.debug("handle_user_input(): command PLACE")
                    valid, x, y, dir = CommandHandler.validate_place_command(command, Board.limit)
                    if valid:
                        self.robot.place(x,y,dir)                        
                    else:
                        logging.info("handle_user_input(): invalid place instruction entered by user - {}".format(command))

                elif command == 'MOVE':
                    logging.debug("handle_user_input(): command MOVE")
                    self.robot.move()

                elif command == 'LEFT':
                    logging.debug("handle_user_input(): command LEFT")
                    self.robot.change_direction('left')

                elif command == 'RIGHT':
                    logging.debug("handle_user_input(): command RIGHT")
                    self.robot.change_direction('right')

                elif command == 'REPORT':
                    logging.debug("handle_user_input(): command REPORT")
                    self.robot.report()

                elif command == 'EXIT':
                    logging.debug("handle_user_input(): command EXIT")
                    print('Exiting Robot App...')
                    exit = True

                else:
                    #Ignore
                    logging.info("handle_user_input(): invalid instruction entered by user - {}".format(command))                                       
                    
                print("")

            except Exception as e:                
                logging.error("handle_user_input(): EXCEPTION {}".format(e))


    @staticmethod
    def validate_place_command(command, limit):
        invalid = (False, None, None, None)

        params = command.split(' ')
        if len(params) <= 1:
            return invalid

        if params[0] != 'PLACE':
            return invalid

        p_str = ""
        for p in params[1:]:
            p_str += p

        args = p_str.split(',')
        if len(args) != 3:
            return invalid

        valid_x, x = CommandHandler.validate_int(args[0], limit)
        if not valid_x:
            return invalid

        valid_y, y = CommandHandler.validate_int(args[1], limit)
        if not valid_y:
            return invalid

        valid_dir, dir = CommandHandler.validate_direction(args[2])                    
        if not valid_dir:
            return invalid

        return (True, x, y, dir)


    @staticmethod
    def validate_int(value, limit):
        try:
            number = int(value.strip())
            if number>=0 and number<=limit:
                return (True, number)
        except ValueError:
            return (False, None)
        
        return (False, None)


    @staticmethod
    def validate_direction(value):
        value = value.strip().lower()
        valid_directions = Direction.get_values()
        
        if value in valid_directions:
            return (True, Direction(value))
        else:
            return (False, None)