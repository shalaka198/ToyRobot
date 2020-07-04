import os
import logging
import argparse
from app.models.board import Board
from app.models.robot import Robot
from app.handlers.input_handler import handle_user_input

def initilise_app():
    print('******************************************')
    print('**** Welcome to Robot App ****')
    print('******************************************')

    board_dimension = 5 #todo:load from settings
    board = Board(board_dimension)
    robot = Robot(-1,-1,None)
    handle_user_input(board, robot)


def main():
    # todo: setup logging

    initilise_app()  


if __name__ == '__main__':
    main()