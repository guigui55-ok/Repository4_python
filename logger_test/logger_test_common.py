#!/usr/bin/python
# -*- coding: utf-8 -*-
"""logger_test_common.py - 
logging.Logger クラス を使用するサンプル
設定値がいろいろあるのでクラス化してみる
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

class logger_info():
    logger : Logger = None
    logger_name : str = ''
    log_file_name : str = ''
    log_format : str = ''
    log_level : int = ''
    def __init__(self) -> None:
        pass

# https://qiita.com/propella/items/5ad25eca11de2a871a06
class logger_util():
    """ logger_util : logger Utility
    """
    logger_info_main : logger_info = None
    logger_info_exp : logger_info = None
    def __init__(self) -> None:
        """not recommended"""
        pass

    def __init__(self,logger_name:str ='',config_file_path:str='') -> None:
        """not recommended"""
        if config_file_path != '':
            self.set_config(config_file_path)
        if logger_name != '':
            self.initialize(logger_name)

    def __init__(self,
                logger_name:str,
                log_file_name:str,
                log_level:int,
                log_format:str,
                handler_mode:int)->None:
        # 変数をメイン logger_info に格納する
        self.logger_info_main = logger_info()
        self.logger_info_main.logger = getLogger(logger_name)
        self.logger_info_main.logger_name = logger_name
        self.logger_info_main.log_file_name = log_file_name
        self.logger_info_main.log_format = log_format
        self.logger_info_main.log_level = log_level
        # log_level より必要なハンドラーリストを取得する
        handler_list = self.create_handler(
            handler_mode,
            self.logger_info_main.log_file_name
        )
        # handler を logger に紐づけする
        for hdr in handler_list:
            self.initialize_logger(
                self.logger_info_main.logger,
                hdr,
                self.logger_info_main.log_level,
                self.logger_info_main.log_format
            )
    
    def initialize_logger_info_for_exception(
        self,
        logger_name:str,
        log_file_name:str,
        log_level:int,
        log_format:str,
        handler_mode:int
    )->None:
        # 変数を logger_info_exp に格納する
        self.logger_info_exp = logger_info()
        self.logger_info_exp.logger_name = logger_name
        self.logger_info_exp.log_file_name = log_file_name
        self.logger_info_exp.log_format = log_format
        self.logger_info_exp.log_level = log_level
        self.logger_info_exp = self.initialize_logger_info(
            self.logger_info_exp,handler_mode
        )
    
    def debug(self,value): self.logger_info_main.logger.debug(value)
    def info(self,value): self.logger_info_main.logger.info(value)
    def warning(self,value): self.logger_info_main.logger.warning(value)
    def error(self,value): self.logger_info_exp.logger.error(value)
    def critical(self,value): self.logger_info_exp.logger.critical(value)

    def initialize_logger_info(
            self,
            arg_logger_info:logger_info,
            handler_mode:int
        ) -> logger_info:
        """ logger_info,handler_mode より logger_info を initialize する
        """
        arg_logger_info.logger = getLogger(arg_logger_info.logger_name)
        handler_list = self.create_handler(
            handler_mode,
            arg_logger_info.log_file_name
        )
        for hdr in handler_list:
            self.initialize_logger(
                arg_logger_info.logger,
                hdr,
                arg_logger_info.log_level,
                arg_logger_info.log_format
            )
        return arg_logger_info

    def initialize_logger(self,
                            logger:Logger,
                            handler:logging.Handler,
                            log_level:int,
                            log_format:str):
        """logger を initialize する
        """
        handler.setLevel(self.cnv_level(log_level))
        formatter = logging.Formatter(log_format)
        handler.setFormatter(formatter)
        logger.addHandler(handler)


    
    def set_streamhandler(self,logger:Logger,log_level:int,log_format:str):
        """not recommended"""
        # sh = StreamHandler(sys.stdout)
        hdr = StreamHandler()
        hdr.setLevel(self.cnv_level(log_level))
        formatter = logging.Formatter(log_format)
        hdr.setFormatter(formatter)
        logger.addHandler(hdr)

    # def set_filehandler(self,logger:Logger):
    #     pass

    def create_handler(self,handler_mode:int,log_file_name:str):
        """handler を取得する"""
        handler_list:Handler = []
        if self.is_nth_bit_set(handler_mode,int(logger_const.STREAM_HANDLER)):
            handler_list.append(StreamHandler())
        if self.is_nth_bit_set(handler_mode,int(logger_const.FILE_HANDLER)):
            handler_list.append(FileHandler(log_file_name,"a"))
            
        return handler_list

    def cnv_level(self,level:int) -> int:
        """ logger_const 定数から logging 定数へ変換する"""
        if(level == logger_const.LEVEL_CRITICAL): return logging.CRITICAL
        elif(level == logger_const.LEVEL_ERROR): return logging.ERROR
        elif(level == logger_const.LEVEL_WARNING): return logging.WARNING
        elif(level == logger_const.LEVEL_INFO): return logging.INFO
        elif(level == logger_const.LEVEL_DEBUG): return logging.DEBUG
        else: return logging.NOTSET

    def is_nth_bit_set(self,num: int, n: int) -> bool:
        """ n が num に含まれているか判定する"""
        if num | (1 << n):
            return True
        return False
        
    # def initialize(self,logger_name:str) -> Logger:
    #     logger = getLogger(logger_name)
    #     return logger

    def initialize(self,logger_name:str) -> Logger:
        """not recommended"""
        self.logger_name = logger_name
        self.logger_info_main = getLogger(self.logger_name)
        sh = StreamHandler(sys.stdout)
        self.__logger.addHandler(sh)
        self.logger_info_main.info('*** logger_class __init__ ***')
        return self.logger_info_main
    
    def get_logger_exp(self) -> Logger:
        """Logger object (exception) を取得する"""
        return self.logger_info_exp.logger

    def get_logger_main(self) -> Logger:
        """Logger object (main) を取得する"""
        return self.logger_info_main.logger

    def get_root_logger(self) -> Logger:
        """Logger object を取得する (return getLogger()) """
        return getLogger()

    def get_logger_from_logging(self,name:str) -> Logger:
        """Logger object を取得する (return getLogger(name)) """
        return getLogger(name)
        
    def set_config(self,path : str):
        """ 設定ファイルを読み込む
            with open(path, "r", encoding="utf-8") as f:
                config.dictConfig(json.load(f))
        """
        # logging クラスの挙動を設定するための json ファイルを読み込む
        with open(path, "r", encoding="utf-8") as f:
            config.dictConfig(json.load(f))

def logger_init_before(name):
    """not recommended"""
    logger = getLogger(name)
    logger.info('*** logger_init ***')
    sh = StreamHandler(sys.stdout)
    logger.addHandler(sh)
    return logger

def logger_init(name) -> logger_util:
    """not recommended"""
    logger = logger_util(name)
    return logger


def set_logger_config(log : Logger,path : str):
    """not recommended"""
    log.info('*** set_logger_config ***')
    # logging クラスの挙動を設定する json ファイルを読み込む
    log_config_name = './log_test3/log_config3.json'
    with open(log_config_name, "r", encoding="utf-8") as f:
        config.dictConfig(json.load(f))


import datetime

def log_test_main_for_logger_class(logger_class:logger_util):
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