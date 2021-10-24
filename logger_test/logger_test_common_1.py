#!/usr/bin/python
# -*- coding: utf-8 -*-
"""logger_test_common_1.py - 
logging.Logger クラス を使用するサンプル
設定値がいろいろあるのでクラス化してみる
logger_test_common_1 から試行錯誤
"""
from logging import  FileHandler, Handler, getLogger
from logging import config
from logging import StreamHandler
from logging import getLogger
from logging import Logger
import logging
import sys
import json
from enum import Enum
from enum import IntEnum

class logger_const(IntEnum):
    STREAM_HANDLER = 0b0001
    FILE_HANDLER = 0b0010
    LEVEL_CRITICAL = 101
    LEVEL_ERROR = 102
    LEVEL_WARNING = 103
    LEVEL_INFO = 104
    LEVEL_DEBUG = 105
    LEVEL_NOTSET = 106

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

    def __init__(self,
                logger_name:str,
                log_file_name:str,
                log_level:int,
                log_format:str,
                handler_mode:int,
                config_file_path:str='')->None:

        if config_file_path != '':
            self.set_config(config_file_path)

        logger = getLogger(logger_name)
        self.__logger = logger
        handler_list = self.create_handler(handler_mode,log_file_name)
        for hdr in handler_list:
            self.set_handler_to_logger(
                self.__logger,hdr,log_level,log_format)
        # if(logger_const.STREAM_HANDLER | handler_mode):
        #     self.set_streamhandler(logger,log_level,log_format)
        # if(logger_const.FILE_HANDLER | handler_mode):
        #     self.set_filehandler(logger)

    def set_handler_to_logger(self,
                            logger:Logger,
                            handler:logging.Handler,
                            log_level:int,
                            log_format:str):
        handler.setLevel(self.cnv_level(log_level))
        formatter = logging.Formatter(log_format)
        handler.setFormatter(formatter)
        logger.addHandler(handler)


    def set_streamhandler(self,logger:Logger,log_level:int,log_format:str):
        # sh = StreamHandler(sys.stdout)
        hdr = StreamHandler()

        hdr.setLevel(self.cnv_level(log_level))
        formatter = logging.Formatter(log_format)
        hdr.setFormatter(formatter)
        logger.addHandler(hdr)

    def set_filehandler(self,logger:Logger):
        pass

    def create_handler(self,handler_mode:int,log_file_name:str):
        handler_list:Handler = []
        if self.is_nth_bit_set(handler_mode,int(logger_const.STREAM_HANDLER)):
            handler_list.append(StreamHandler())
        if self.is_nth_bit_set(handler_mode,int(logger_const.FILE_HANDLER)):
            self.create_file(log_file_name)
            handler_list.append(FileHandler(log_file_name,"a"))
            
        print('len(handler_list)= '+str(len(handler_list)))
        return handler_list

    def cnv_level(self,level:int) -> int:
        if(level == logger_const.LEVEL_CRITICAL): return logging.CRITICAL
        elif(level == logger_const.LEVEL_ERROR): return logging.ERROR
        elif(level == logger_const.LEVEL_WARNING): return logging.WARNING
        elif(level == logger_const.LEVEL_INFO): return logging.INFO
        elif(level == logger_const.LEVEL_DEBUG): return logging.DEBUG
        else: return logging.NOTSET

    def is_nth_bit_set(self,num: int, n: int) -> bool:
        if num | (1 << n):
            return True
        return False
    
    def create_file(self,file_name:str):        
        with open(file_name, "a", encoding="utf-8") as f:
            f.write('')
        
    # def initialize(self,logger_name:str) -> Logger:
    #     logger = getLogger(logger_name)
    #     return logger

    def initialize(self,logger_name:str) -> Logger:
        self.logger_name = logger_name
        self.__logger = getLogger(self.logger_name)
        sh = StreamHandler(sys.stdout)
        self.__logger.addHandler(sh)
        self.__logger.info('*** logger_class __init__ ***')
        return self.__logger

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

def log_test_main_for_logger_class(logger_class:logger_class):
    logger = logger_class.get_logger()
    log_test_main(logger)

def log_test_main(arglogger:Logger):
    print('---------------------------')
    print( '__file__ = ' + __file__ )
    # logger = Logger(arglogger) 
    logger = arglogger
    # 現在日時（日付と時刻）を取得する
    dt_now = datetime.datetime.now()
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
    logger.critical('critical')
    logger.info('Process End!')
    try:
        int("aaa")
    except:
        #logging.exception(e) # NG
        logger.exception("What is doing when exception happens.")
    
    #logger.info('logger.__format__ = '+ logger.__format__())
    # logger.__format__('%(asctime)s - %(levelname)s - %(message)s', '%Y-%m-%d %H:%M:%S')
    # buf = logger.__format__('%(asctime)s')
    # logger.critical('logger.__format__ = '+ str(buf))
    # if logger.hasHandlers:
    #     print('logger.hasHandlers = true')
        # for i, handler in logger.hasHandlers:
        #     print(handler)
        # ch = logging.FileHandler(logger_class.__logger)
        
        # ch.emit(logging.LogRecord())