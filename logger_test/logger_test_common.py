
from logging import getLogger
from logging import config
from logging import StreamHandler
from logging import getLogger
from logging import Logger
import logging
import sys
import json

# https://qiita.com/propella/items/5ad25eca11de2a871a06
class logger_class():
    __logger:Logger = None
    logger_name = ''
    # logger_file_path=''
    def __init__(self) -> None:
        pass

    def __init__(self,logger_name:str ='',config_file_path:str='') -> None:
        if config_file_path != '':
            self.set_config(config_file_path)
        if logger_name != '':
            self.initialize(logger_name)

    def initialize(self,logger_name : str):
        self.logger_name = logger_name
        self.__logger = getLogger(self.logger_name)
        sh = StreamHandler(sys.stdout)
        self.__logger.addHandler(sh)
        self.__logger.info('*** logger_class __init__ ***')

    def get_logger(self) -> Logger:
        return self.__logger

    def get_root_logger(self) -> Logger:
        return getLogger()

    def get_logger_from_logging(self,name:str) -> Logger:
        return getLogger(name)
        
    def set_config(self,path : str):
        # logging クラスの挙動を設定するための json ファイルを読み込む
        with open(path, "r", encoding="utf-8") as f:
            config.dictConfig(json.load(f))

def logger_init_before(name):
    logger = getLogger(name)
    logger.info('*** logger_init ***')
    sh = StreamHandler(sys.stdout)
    logger.addHandler(sh)
    return logger

def logger_init(name) -> logger_class:
    logger = logger_class(name)
    return logger


def set_logger_config(log : Logger,path : str):
    log.info('*** set_logger_config ***')
    # logging クラスの挙動を設定する json ファイルを読み込む
    log_config_name = './log_test3/log_config3.json'
    with open(log_config_name, "r", encoding="utf-8") as f:
        config.dictConfig(json.load(f))


import datetime
def log_test_main(logger_class : logger_class):
    print('---------------------------')
    print( '__file__ = ' + __file__ )

    # 現在日時（日付と時刻）を取得する
    dt_now = datetime.datetime.now()

    logger = logger_class.get_logger()
    logger.info(str(dt_now))
    logger.info('message')

    logger.info('*** log_test_main ***')

    # ロガーのログレベルをWARNINGに設定する
    # logger.setLevel(logger.WARNING)

    logger.info('Process Start!')
    logger.debug('debug')
    logger.info('info')
    logger.warning('warning')
    logger.error('error')
    logger.info('Process End!')
    try:
        int("aaa")
    except:
        logger.exception("What is doing when exception happens.")
    
    if logger.hasHandlers:
        print('logger.hasHandlers = true')
        # for i, handler in logger.hasHandlers:
        #     print(handler)
        ch = logging.FileHandler(logger_class.__logger)
        
        ch.emit(logging.LogRecord())