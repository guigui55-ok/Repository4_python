"""logger_test.py - 
logging.Logger クラス を使用するサンプル
コード上でのみ logger クラス設定を実装する
config.dictConfig を使用しない
logger を委譲したクラスを使用しない★
"""
import logging
import logger_test_common
#https://qiita.com/shotakaha/items/0fa2db1dc8253c83e2bb

def logger_test7():
 logger = setup_logger(__name__,'./logger_config/app7.log')
 logger_test_common.log_test_main(logger)

def logger_test7_do(logger : logging.Logger):
    logger_test_common.log_test_main(logger)


def setup_logger(name:str,logfile:str='app.log') -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # create file handler which logs even DEBUG messages
    fh = logging.FileHandler(logfile)
    fh.setLevel(logging.DEBUG)
    fh_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(filename)s - %(name)s - %(funcName)s - %(message)s')
    fh.setFormatter(fh_formatter)

    # create console handler with a INFO log level
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    ch_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', '%Y-%m-%d %H:%M:%S')
    ch.setFormatter(ch_formatter)

    # add the handlers to the logger
    logger.addHandler(fh)
    logger.addHandler(ch)
    return logger

logger_test7()