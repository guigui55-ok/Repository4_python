
from logging import getLogger
from logging import config
import sys
import os  
import json

from logger_test_common import log_test_main, logger_class,logger_init,set_logger_config


def log_test4_main():
    logger = log_test4_init()
    log_test_main(logger)

def log_test4_init():
    print('---------------------------')
    print( '__file__ = ' + __file__ )
    # initialize and set logger config 
    # log_config_name = './log_test3/log_config3.json'
    log_config_name = './logger_config/log_config4.json'
    log_config_name = './logger_config/log_config5.json'
    logger = logger_class(__name__,log_config_name)
    return logger

if __name__ == '__main__':
    print('__name__ = ' + __name__)
    log_test4_main()