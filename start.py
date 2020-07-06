import os
import logging
from datetime import datetime
import argparse
from app.config.config import load_config
from app.models.board import Board
from app.models.robot import Robot
from app.handlers.command_handler import CommandHandler


def setup_logging(conf):    
    log_location = conf['LOGGING']['LOCATION']    
    if not os.path.exists(log_location):
        os.makedirs(log_location) 
    
    log_level = logging.DEBUG
    l = conf['LOGGING']['LEVEL'].strip().upper()
    if(l == 'INFO'):
        log_level = logging.INFO
    elif(l == 'ERROR'):
        log_level = logging.ERROR
    elif(l == ['WARN','WARNING']):
        log_level = logging.WARN
    elif(l in ['CRITICAL','FATAL']):
        log_level = logging.CRITICAL   
    
    logging.basicConfig(level = log_level,
                        filename = log_location + '/robot_' + datetime.now().strftime("%Y%m%d_%H%M%S_%f")+ '.txt',
                        format = '%(levelname)s %(asctime)s %(message)s')    

    logging.debug('setup_logging(): done')


def initilise_app():
    logging.debug('initilise_app(): start')
    
    print('******************************************')
    print('**** Welcome to Robot App ****')
    print('******************************************')

    board_dimension = 5 #todo:load from settings
    commandHandler = CommandHandler(Board(board_dimension), Robot(-1,-1,None))
    commandHandler.handle_user_input()

    logging.debug('initilise_app(): finish')


def main():
    conf = load_config()

    setup_logging(conf)

    initilise_app()  


if __name__ == '__main__':
    main()