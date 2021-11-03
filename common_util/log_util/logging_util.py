# -*- coding: utf-8 -*-
"""logger_util.py - Logger Utility

ログレベル「ERROR,CRITICAL」をログ出力を重複せずに、出力する内容(書式)を変更するためのクラス
"""
 
import logging
from logging import config, exception
import sys
import json
from enum import IntEnum
from enum import Enum

class const_str(Enum):
    DEFAULT_FORMAT = '[%(levelname)s]%(name)s -> %(message)s'
    DEFAULT_FILE_NAME = 'app.log'

class const(IntEnum):
    STREAM_HANDLER = 0b0001
    FILE_HANDLER = 0b0010
    LEVEL_CRITICAL = 101
    LEVEL_ERROR = 102
    LEVEL_WARNING = 103
    LEVEL_INFO = 104
    LEVEL_DEBUG = 105
    LEVEL_NOTSET = 106
    DEFAULT_LEVEL = logging.NOTSET
    DEFAULT_HANDLER = STREAM_HANDLER | FILE_HANDLER

class logger_info():
    logger : logging.Logger = None
    logger_name : str = ''
    log_file_name : str = ''
    log_format : str = ''
    log_level : int = ''
    config_file_path : str = ''
    def __init__(self) -> None:
        pass
    def is_logger_none(self)-> bool:
        if self.logger == None:return True
        return False

class logger_util():
    """ logger_util : logger Utility"""
    logger_info_main : logger_info = None
    logger_info_exp : logger_info = None
    exp : logging.Logger = None
    # -------------------------------------------
    def __init__(self,
                logger_name : str,
                config_file_path : str = '',
                log_file_name : str = const_str.DEFAULT_FILE_NAME.value,
                log_level : int = const.DEFAULT_LEVEL,
                log_format : str = const_str.DEFAULT_FORMAT.value,
                handler_mode : int = const.DEFAULT_HANDLER)->None:
        self.logger_info_main = logger_info()
        if(config_file_path != '') & (config_file_path != None):
            # config ファイルを使用するときは、ファイル読み込み後 getloggerすること
            self.set_config(config_file_path)  
            self.logger_info_main.logger  = logging.getLogger(logger_name)
            self.logger_info_main.logger_name = logger_name
            self.logger_info_main.config_file_path = config_file_path

        else:
            # root Logger で level 以上のログを取得するように設定する
            logging.getLogger().setLevel(logging.NOTSET)
            self.logger_info_main.logger = logging.getLogger(logger_name)        
            
            # 変数をメイン logger_info に格納する
            self.logger_info_main.logger_name = logger_name
            self.logger_info_main.log_file_name = log_file_name
            self.logger_info_main.log_format = log_format
            self.logger_info_main.log_level = log_level
            # log_level より必要な handler リストを取得する
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
    
    ################################################
    def initialize_logger_info_for_exception(
        self,
        logger_name:str,
        log_file_name:str,
        log_level:int,
        log_format:str,
        handler_mode:int
    )->None:
        """ logger_info_main とは別の logger を self.logger_info_exp に作成する"""
        # 変数を logger_info_exp に格納する
        self.logger_info_exp = logger_info()
        self.logger_info_exp.logger_name = logger_name
        self.logger_info_exp.log_file_name = log_file_name
        self.logger_info_exp.log_format = log_format
        self.logger_info_exp.log_level = log_level
        self.logger_info_exp = self.initialize_logger_info(
            self.logger_info_exp,handler_mode
        )
        self.exp = self.logger_info_exp.logger
    
    # -------------------------------------------
    def initialize_logger_info(
            self,
            arg_logger_info:logger_info,
            handler_mode:int
        ) -> logger_info:
        """ logger_info,handler_mode より logger_info を initialize する
        """
        # logger を new する
        arg_logger_info.logger = \
            logging.getLogger(arg_logger_info.logger_name)
        ## handler は複数紐づける場合があるのでリストで処理をする
        # handler リストを取得する
        handler_list = self.create_handler(
            handler_mode,
            arg_logger_info.log_file_name
        )
        # handler と logger を紐づける。level、format もセットする
        for hdr in handler_list:
            self.initialize_logger(
                arg_logger_info.logger,
                hdr,
                arg_logger_info.log_level,
                arg_logger_info.log_format
            )
        return arg_logger_info

    # -------------------------------------------
    def initialize_logger(self,
                            logger:logging.Logger,
                            handler:logging.Handler,
                            log_level:int,
                            log_format:str) -> logging.Logger:
        """logger を initialize する
        """
        
        handler.setLevel(self.cnv_level(log_level))
        formatter = logging.Formatter(str(log_format))
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        return logger

    # def initialize_logger_for_config(
    #     self,
    #     handler_mode : int,
    #     logger : logging.Logger
    # ):
    #     handler_list = self.create_handler(
    #         handler_mode,
    #         ''
    #     )
    #     # handler と logger を紐づける。level、format もセットする
    #     for hdr in handler_list:
    #         logger.addHandler(hdr)


    # -------------------------------------------
    def debug(self,value): self.logger_info_main.logger.debug(value)
    def info(self,value): self.logger_info_main.logger.info(value)
    def warning(self,value): self.logger_info_main.logger.warning(value)
    def error(self,value): 
        try:                
            if self.logger_info_exp == None:
                self.logger_info_main.logger.error(value)
            else:
                if not self.logger_info_exp.is_logger_none():
                    self.logger_info_exp.logger.error(value)
                else:
                    self.logger_info_main.logger.error(value)
                    self.logger_info_main.logger.error('logger_util.logger_info_exp is None!')
        except Exception as e:
            print(e) 

    def critical(self,value):
        try:
            if self.logger_info_exp == None:
                self.logger_info_main.logger.critical(value)
            else:
                if not self.logger_info_exp.is_logger_none():
                    self.logger_info_exp.logger.critical(value)
                else:
                    self.logger_info_main.critical(value)
                    self.logger_info_main.critical('logger_util.logger_info_exp is None!')
        except Exception as e:
            print(e)


    
    # def set_streamhandler(self,logger:logging.Logger,log_level:int,log_format:str):
    #     """not recommended"""
    #     # sh = StreamHandler(sys.stdout)
    #     hdr = logging.StreamHandler()
    #     hdr.setLevel(self.cnv_level(log_level))
    #     formatter = logging.Formatter(log_format)
    #     hdr.setFormatter(formatter)
    #     logger.addHandler(hdr)

    # def set_filehandler(self,logger:Logger):
    #     pass

    def create_handler(self,handler_mode:int,log_file_name:str):
        """handler を取得する"""
        handler_list:logging.Handler = []
        if self.is_nth_bit_set(handler_mode,int(const.STREAM_HANDLER)):
            handler_list.append(logging.StreamHandler())
        if self.is_nth_bit_set(handler_mode,int(const.FILE_HANDLER)):
            if (log_file_name != '') & (log_file_name != None):
                handler_list.append(logging.FileHandler(log_file_name,"a"))
            else:
                print('log_file_name is nothing(length=0 or None)')
                pass
                #handler_list.append(logging.FileHandler())
            
        return handler_list

    def cnv_level(self,level:int):
        """ logger_const 定数から logging 定数へ変換する"""
        if(level == const.LEVEL_CRITICAL): return logging.CRITICAL
        elif(level == const.LEVEL_ERROR): return logging.ERROR
        elif(level == const.LEVEL_WARNING): return logging.WARNING
        elif(level == const.LEVEL_INFO): return logging.INFO
        elif(level == const.LEVEL_DEBUG): return logging.DEBUG
        else: return logging.NOTSET

    def is_nth_bit_set(self,num: int, n: int) -> bool:
        """ n が num に含まれているか判定する"""
        if num | (1 << n):
            return True
        return False
        
    # def initialize(self,logger_name:str) -> Logger:
    #     logger = getLogger(logger_name)
    #     return logger

    # def initialize(self,logger_name:str) -> logging.Logger:
    #     """not recommended"""
    #     self.logger_name = logger_name
    #     self.logger_info_main = logging.getLogger(self.logger_name)
    #     sh = logging.StreamHandler(sys.stdout)
    #     self.__logger.addHandler(sh)
    #     self.logger_info_main.info('*** logger_class __init__ ***')
    #     return self.logger_info_main
    
    def get_logger_exp(self) -> logging.Logger:
        """Logger object (exception) を取得する"""
        return self.logger_info_exp.logger

    def get_logger_main(self) -> logging.Logger:
        """Logger object (main) を取得する"""
        return self.logger_info_main.logger

    def get_root_logger(self) -> logging.Logger:
        """Logger object を取得する (return getLogger()) """
        return logging.getLogger()

    def get_logger_from_logging(self,name:str) -> logging.Logger:
        """Logger object を取得する (return getLogger(name)) """
        return logging.getLogger(name)
        
    def set_config(self,path : str):
        """ 設定ファイルを読み込む
            with open(path, "r", encoding="utf-8") as f:
                config.dictConfig(json.load(f))
        """
        # logging クラスの挙動を設定するための json ファイルを読み込む
        with open(path, "r", encoding="utf-8") as f:
            config.dictConfig(json.load(f))

def intialize_logger_util(
    log_file_name : str,
    config_file_path : str,
    basic_log_format : str,
    exception_log_format : str
)-> logger_util:
    format = basic_log_format
    loggeru = logger_util(
        __name__,
        config_file_path,
        log_file_name,        
        const.LEVEL_NOTSET,
        format,
        const.FILE_HANDLER |
        const.STREAM_HANDLER
    )
    
    format = exception_log_format
    loggeru.initialize_logger_info_for_exception(
        __name__ + 'exp',
        log_file_name,
        const.LEVEL_ERROR,
        format,
        const.FILE_HANDLER |
        const.STREAM_HANDLER
    )
    return loggeru

# def logger_init_before(name):
#     """not recommended"""
#     logger = getLogger(name)
#     logger.info('*** logger_init ***')
#     sh = logging.StreamHandler(sys.stdout)
#     logger.addHandler(sh)
#     return logger

# def logger_init(name) -> logger_util:
#     """not recommended"""
#     logger = logger_util(name)
#     return logger


# def set_logger_config(log : logging.Logger,path : str):
#     """not recommended"""
#     log.info('*** set_logger_config ***')
#     # logging クラスの挙動を設定する json ファイルを読み込む
#     log_config_name = './log_test3/log_config3.json'
#     with open(log_config_name, "r", encoding="utf-8") as f:
#         logging.config.dictConfig(json.load(f))


# import datetime

# def log_test_main_for_logger_class(logger_class:logger_util):
#     logger = logger_class.get_logger()
#     log_test_main(logger)

# def log_test_main(arglogger:Logger):
#     print('---------------------------')
#     print( '__file__ = ' + __file__ )
#     # logger = Logger(arglogger) 
#     logger = arglogger
#     # 現在日時（日付と時刻）を取得する
#     dt_now = datetime.datetime.now()
#     logger.info(str(dt_now))
#     logger.info('message')

#     logger.info('*** log_test_main ***')

#     # ロガーのログレベルをWARNINGに設定する
#     # logger.setLevel(logger.WARNING)

#     logger.info('Process Start!')
#     logger.debug('debug')
#     logger.info('info')
#     logger.warning('warning')
#     logger.error('error')
#     logger.critical('critical')
#     logger.info('Process End!')
#     try:
#         int("aaa")
#     except:
#         #logging.exception(e) # NG
#         logger.exception("What is doing when exception happens.")
    
#     #logger.info('logger.__format__ = '+ logger.__format__())
#     # logger.__format__('%(asctime)s - %(levelname)s - %(message)s', '%Y-%m-%d %H:%M:%S')
#     # buf = logger.__format__('%(asctime)s')
#     # logger.critical('logger.__format__ = '+ str(buf))
#     # if logger.hasHandlers:
#     #     print('logger.hasHandlers = true')
#         # for i, handler in logger.hasHandlers:
#         #     print(handler)
#         # ch = logging.FileHandler(logger_class.__logger)
        
#         # ch.emit(logging.LogRecord())