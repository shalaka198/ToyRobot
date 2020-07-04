from app.models.board import Board
from app.models.robot import Robot
from app.models.direction import Direction

#class CommandHandler:

def handle_user_input(board:Board, robot:Robot):
    exit = False
    while(not exit):        
        print("*******************************************************************************")
        print("Please enter one of the following valid instruction")
        print("1.'PLACE X,Y,F': Places robot at x,y location on the board facing one of north, south, east or west direction")
        print("Valid values for X and Y are between 0 and {}".format(board.dimension-1))
        print("F can have one of these values: {}".format(Direction.get_values()))
        print("2.'MOVE': Moves robot 1 unit forward in the direction it is facing")
        print("3.'LEFT': Rotates the robot 90 degrees in the left direction")
        print("4.'RIGHT': Rotates the robot 90 degrees in the right direction")
        print("5.'REPORT': Prints robot location (x,y) and direction in which it is facing")
        print("6.'EXIT': Exits the App")
        print("*******************************************************************************")

        command = input("What's your instruction instruction:").strip().upper()
        try:
            if command.startswith('PLACE'):
                valid, x, y, dir = validate_place_command(command, board.dimension-1)
                if valid:
                    robot.place(x,y,dir)
                else:
                    print('Invalid place instruction')
            elif command == 'MOVE':
                robot.move()
            elif command == 'LEFT':
                robot.change_direction('left')
            elif command == 'RIGHT':
                robot.change_direction('right')
            elif command == 'REPORT':
                robot.report()
            elif command == 'EXIT':
                print('Exiting Robot App...')
                exit = True
            else:
                print("*****Please enter a valid instruction")
                
            print("")

        except Exception as e:
            #todo:
            print("EXCEPTION {}".format(e))


def validate_place_command(command, limit):
    params = command.split(' ')[1].split(',')
    print(params)
    valid_x, x = validate_int(params[0], limit)
    if not valid_x:
        return (False, None, None, None)

    valid_y, y = validate_int(params[1], limit)
    if not valid_y:
        return (False, None, None, None)

    valid_dir, dir = validate_direction(params[2])                    
    if not valid_dir:
        return (False, None, None, None)

    return (True, x, y, dir)

def validate_int(value, limit):
    try:
        number = int(value.strip())
        if number>=0 and number<=limit:
            return (True, number)
    except ValueError:
        return (False, None)
    
    return (False, None)

def validate_direction(value):
    value = value.strip().lower()
    print(value)
    valid_directions = Direction.get_values()
    print(valid_directions)
    if value in valid_directions:
        return (True, Direction(value))
    else:
        return (False, None)