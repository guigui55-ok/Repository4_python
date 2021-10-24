"""logger_test.py - 
logging.Logger クラス を使用するサンプル
config.dictConfig を使用
"""
from logging import getLogger
from logging import config
from logging import StreamHandler
import sys
import os  
import json


def log_test1():
    
    # logging クラスの挙動を設定する json ファイルを読み込む
    log_config_name = 'logconfig.json'
    with open(log_config_name, "r", encoding="utf-8") as f:
        config.dictConfig(json.load(f))

    # 悪い例
    # logger = logging.getLogger(__name__)
    # sh = logging.StreamHandler(sys.stdout)
    
    # よい例
    logger = getLogger(__name__)
    logger.info('message')

    # sh = StreamHandler(sys.stdout)
    # logger.addHandler(sh)


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


"""
https://www.python.ambitious-engineer.com/archives/725
ログの設定使用できる設定ファイルには
yaml形式、ini形式、json形式がある
※設定値について
https://ahyt910.hateblo.jp/entry/2019/04/16/170339
version：現在指定できる値は1のみ。今後のバージョンアップ時の後方互換性確保のための項目。
disable_existing_loggers
　True:既存のLoggerと同名の新規Loggerを使用不可にする。
　False: 既存のLoggerを上書きして新規Loggerとして使用可能にする。

root:
handlers
　　handeler IDを定義する
    logFileHandler: 
    consoleHandler: 
incremental ：　既存の logger についている handler や filter などを削除せずに追加だけを行います。
propagate=1　１：上位のロガーに伝番できる、0できない
qualname=compiler.parser　このロガーを取得する際に使う名前


 "formatters"　ログ出力の際のフォーマットID、フォーマットを定義する
 "formatters": {
    "consoleFormatter": {
      "format": "[%(levelname)-8s]%(funcName)s - %(message)s"
    },
    "logFileFormatter": {
      "format": "%(asctime)s|%(levelname)-8s|%(name)s|%(funcName)s|%(message)s"
    }
    formatters:
  brief:　format名
    format: '%(message)s'
  default:
    format: '%(asctime)s %(levelname)-8s %(name)-15s %(message)s'
    datefmt: '%Y-%m-%d %H:%M:%S'

filters:　フィルターID、フィルターを定義する
　Loggerが受け取ったLogRecordを出力するか否かを判断するために使用するものがログフィルター
  "filters": {
    "filterExample": {
      "()": "",
      "words": [
        "password",
        "secret"
      ]
    }
  }

dict["handlers"][**]["class"]
　logging.StreamHandler
　logging.FileHandler

level
　DEBUG：Debug以上をファイルに書き出し
　INFO：Info以上を標準出力に書き出し

※console 出力時の設定値
　"class": "logging.StreamHandler"
　"stream": "ext://sys.stdout"
　filters:任意のフィルタID
　level：任意のログLevel
　formatter:任意のフォーマットID

※file 出力時の設定値
　"class": "logging.FileHandler"
  class : logging.handlers.RotatingFileHandler
　"filename": "./log/app.log"　　ファイル名、パス指定可
　"mode": "w",　　書き込みモード
　"encoding": "utf-8"　　文字エンコード
  maxBytes: 1024
  backupCount: 3
　filters:任意のフィルタID
　level：任意のログLevel
　formatter:任意のフォーマットID


https://docs.python.org/ja/3/library/logging.config.html
カスタム'()'として定義することで、コード上から、指定可能
 custom:
      (): my.package.customFormatterFactory
      bar: baz
      spam: 99.9
      answer: 42
my.package.customFormatterFactory(bar='baz', spam=99.9, answer=42)

※こういう記載もできる
handlers:
  email:
    class: logging.handlers.SMTPHandler
    mailhost: localhost
    fromaddr: my_app@domain.tld
    toaddrs:
      - support_team@domain.tld
      - dev_team@domain.tld
    subject: Houston, we have a problem.
"""