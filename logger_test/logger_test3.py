"""logger_test.py - 
logging.Logger クラス を使用するサンプル
config.dictConfig を使用
logger を委譲したクラスを使用★
"""
from logging import getLogger
from logging import config
import sys
import os  
import json

from logger_test_common_1 import log_test_main, logger_class,logger_init,set_logger_config


def log_test3_main():
    logger = log_test3_init()
    log_test_main(logger)

def log_test3_init():
    print('---------------------------')
    print( '__file__ = ' + __file__ )
    logger = logger_class()
    # set logger config 
    log_config_name = './log_test3/log_config3.json'
    logger.set_config(log_config_name)
    # initialize logger
    logger.initialize(__name__)
    return logger

if __name__ == '__main__':
    print('__name__ = ' + __name__)
    log_test3_main()