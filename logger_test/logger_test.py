
from logging import getLogger
from logging import config
from logging import StreamHandler
import sys
import os  
import json

def log_test1():
    
    # 悪い例
    # logger = logging.getLogger(__name__)
    # sh = logging.StreamHandler(sys.stdout)
    print(os.getcwd())
    log_config_name = 'logconfig.json'
    with open(log_config_name, "r", encoding="utf-8") as f:
        config.dictConfig(json.load(f))
        pass

    # よい例
    logger = getLogger(__name__)
    logger.info('message')

    sh = StreamHandler(sys.stdout)
    logger.addHandler(sh)


    # ロガーのログレベルをWARNINGに設定する
    # logger.setLevel(logger.WARNING)

    logger.info("this messege is never displayed.") # この行は出力されない

    logger.warning("unauthorized.")

    # default では warning と error はコンソールに出力される
    # logconfig.json 設定ファイルによって、上記動作は変えられる
    logger.info('Process Start!')
    logger.debug('debug')
    logger.info('info')
    logger.warning('warning')
    logger.error('error')
    logger.info('Process End!')
    
log_test1()

# log の 重要度
# 実行クラス、場所などを特定
# 独自のエラーメッセージを記録する
# ファイルに出力する
# コンソールに出力する
# ほかのオブジェクトに渡して使えるように


# logger について
# https://qiita.com/amedama/items/b856b2f30c2f38665701