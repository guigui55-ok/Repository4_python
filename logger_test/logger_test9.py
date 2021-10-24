"""logger_test.py - 
logging.Logger クラス を使用するサンプル
コード上でのみ logger クラス設定を実装する
config.dictConfig を使用しない
logger を委譲したクラスを使用する
logger_test8 から発展させようとしたが→logging_util で試す★
logger_test8 とおなじ
"""
import logging
import logger_test_common
#https://qiita.com/shotakaha/items/0fa2db1dc8253c83e2bb

def logger_test9():
 logger = setup_logger(__name__,'./logger_config/app9.log')
 logger_test_common.log_test_main(logger)


def setup_logger(name:str,log_file_name:str='app.log') -> logging.Logger:
    clogger = logger_test_common.logger_util(
        __name__,
        log_file_name,
        int(logger_test_common.logger_const.LEVEL_ERROR),
        '%(asctime)s - %(message)s',
        logger_test_common.logger_const.FILE_HANDLER 
        | logger_test_common.logger_const.STREAM_HANDLER
    )

    return clogger.get_logger_main()
    # logger = logging.getLogger(name)
    # logger.setLevel(logging.DEBUG)

    # # create file handler which logs even DEBUG messages
    # fh = logging.FileHandler(logfile)
    # fh.setLevel(logging.DEBUG)
    # fh_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(filename)s - %(name)s - %(funcName)s - %(message)s')
    # fh.setFormatter(fh_formatter)

    # # create console handler with a INFO log level
    # ch = logging.StreamHandler()
    # ch.setLevel(logging.INFO)
    # ch_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', '%Y-%m-%d %H:%M:%S')
    # ch.setFormatter(ch_formatter)

    # # add the handlers to the logger
    # logger.addHandler(fh)
    # logger.addHandler(ch)

logger_test9()