import os
import logging
import argparse
from app.models.board import Board
from app.models.robot import Robot
from app.handlers.command_handler import CommandHandler

def initilise_app():
    print('******************************************')
    print('**** Welcome to Robot App ****')
    print('******************************************')

    board_dimension = 5 #todo:load from settings
    commandHandler = CommandHandler(Board(board_dimension), Robot(-1,-1,None))
    commandHandler.handle_user_input()


def main():
    # todo: setup logging

    initilise_app()  


if __name__ == '__main__':
    main()