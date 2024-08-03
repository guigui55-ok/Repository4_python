
"""
簡易的なLogger

Memo:
    メソッドなどはpython標準モジュールLoggerになるべく近くしている
    モジュール下部に使い方を記載している

"""

import datetime

class LogLevel():
    NONE = 0
    CRITICAL = 2
    ERROR = 3
    ALERT = 4
    WARNING = 5
    CAUTION = 6
    INFO = 7
    DEBUG = 8
    DETAIL = 9
    TRACE = 10

NEW_LINE = '\n'
TIME_FORMAT = '%y/%m/%d %H:%M:%S.%F'

class SimpleLogger():
    class LogLevel(LogLevel):
        pass
    DEFAULT_TIME_FORMAT = '%y/%m/%d %H:%M:%S.%F'
    def __init__(self) -> None:
        self.path = ''
        self.log_level = LogLevel.INFO
        self.output_console = True
        self.date_time_format = ''
        self.encoding = ''
        self.set_default_value()
        #/ 
        #検討中
        # あらかじめオリジナルの（LogLeveとは重複しない値の）ログレベルを指定しておいて　
        # info(value, 20)とかすると、任意で出力/抑制できるようにする予定
        self.add_log_level_list = []
    
    def set_default_value(self):
        # シンプルなロガーなので、最初なほぼ何もない状態からとしている
        self.date_time_format = ''
        self.encoding = 'sjis'
        self.log_level = LogLevel.INFO
        self.output_console = True
        self.path = ''

    def critical(self, value):
        if self.log_level>=LogLevel.CRITICAL:
            self._print(value)
    def error(self, value):
        if self.log_level>=LogLevel.ERROR:
            self._print(value)
    def alert(self, value):
        if self.log_level>=LogLevel.ALERT:
            self._print(value)
    def warning(self, value):
        if self.log_level>=LogLevel.WARNING:
            self._print(value)
    def caution(self, value):
        if self.log_level>=LogLevel.CAUTION:
            self._print(value)
    def info(self, value):
        if self.log_level>=LogLevel.INFO:
            self._print(value)
    def debug(self, value):
        if self.log_level>=LogLevel.DEBUG:
            self._print(value)
    def trace(self, value):
        if self.log_level>=LogLevel.TRACE:
            self._print(value)
    def trace(self, value):
        if self.log_level>=LogLevel.TRACE:
            self._print(value)
    
    def _print(self, value):
        value = self._add_time(value)
        print(value)
        self._to_file(value + NEW_LINE)

    def _to_file(self, value):
        """ ファイルパス値があれば、書き込む """
        if self.path!=''and self.path!=None:
            with open(str(self.path), 'a', encoding=self.encoding)as f:
                f.write(value)
    
    def _add_time(self, value):
        """ 日付設定があれば付与する """
        if self.date_time_format!='' and self.date_time_format!=None:
            time_str = datetime.datetime.now().strftime(self.date_time_format)
            ret = '{}    {}'.format(time_str, value)
            return ret
        return value


def _test1():
    # コンソール出力
    logger = SimpleLogger()
    logger.set_default_value()
    logger.info('_test1 info')

def _test2():
    # コンソール出力　＋　ファイル出力
    #パスを設定したときファイル出力をする
    logger = SimpleLogger()
    logger.set_default_value()
    from pathlib import Path
    path = Path(__file__).parent.joinpath('__test_log.txt')
    logger.path = path
    logger.info('_test2 info')
    print('logger.path = {}'.format(logger.path))

def _test3():
    # コンソール出力　＋　ファイル出力　+ 日付出力
    #date_time_formatを設定したとき日付出力をする
    logger = SimpleLogger()
    logger.set_default_value()
    #/
    from pathlib import Path
    path = Path(__file__).parent.joinpath('__test_log.txt')
    logger.path = path
    #/
    logger.date_time_format = TIME_FORMAT
    logger.info('_test3 info')
    print('logger.path = {}'.format(logger.path))

if __name__ == '__main__':
    _test1()
    _test2()
    _test3()