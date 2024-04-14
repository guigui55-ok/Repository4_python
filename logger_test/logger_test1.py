"""
logger_test.py - 

logging.Logger クラス を使用するサンプル
    config.dictConfig を使用★
    logger_test とおなじ
    logger を委譲したクラスを使用しない★
"""
from logging import getLogger
from logging import config
from logging import StreamHandler
import sys
import os  
import json


def log_test1():
    print('---------------------------')
    print('*** log_test1 ***')
    print( '__file__ = ' + __file__ )
    # logging クラスの挙動を設定する json ファイルを読み込む
    log_config_name = './log_test2/log_config2.json'
    with open(log_config_name, "r", encoding="utf-8") as f:
        config.dictConfig(json.load(f))
    
    logger = getLogger(__name__)
    logger.info('message')

    sh = StreamHandler(sys.stdout)
    logger.addHandler(sh)

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

