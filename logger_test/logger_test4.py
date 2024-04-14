"""
logger_test.py - 

logging.Logger クラス を使用するサンプル
    config.dictConfig を使用しない★
    logger を委譲したクラスを使用
"""
from logging import getLogger
from logging import config
import sys
import os  
import json

from logger_test_common_1 import log_test_main, logger_class,logger_init,set_logger_config
import logger_test_common_1

def log_test4_main():
    logger = log_test4_init()
    log_test_main(logger.get_logger())

def log_test4_init():
    print('---------------------------')
    print( '__file__ = ' + __file__ )
    # initialize and set logger config 
    # log_config_name = './log_test3/log_config3.json'
    log_config_name = './logger_config/log_config4.json'
    log_config_name = './logger_config/log_config5.json'
    log_config_name = './logger_config/log_config6.json'
    log_config_name = './logger_config/log_config8.json'
    import os
    path = os.getcwd() + r"\logger_config\app4.log"
    logger = logger_class(
        __name__,
        path,
        logger_test_common_1.logger_const.LEVEL_DEBUG,
        '%(levelname)s:%(name)s:%(message)s',
        logger_test_common_1.logger_const.FILE_HANDLER |
        logger_test_common_1.logger_const.STREAM_HANDLER,
        log_config_name)
    return logger

if __name__ == '__main__':
    print('__name__ = ' + __name__)
    log_test4_main()