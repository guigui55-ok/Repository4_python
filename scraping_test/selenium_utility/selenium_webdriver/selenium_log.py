
"""
Selenium_webdriver webdriver_utility を使用時のログ出力モジュール

依存package
 common_utility.log_util.loggin_util
  html_log.html_logger
"""

import datetime
import pathlib
from pathlib import Path
#/
# C:\Users\OK\source\repos\Repository4_python\scraping_test\html_log
# C:\Users\OK\source\repos\Repository4_python\scraping_test\selenium_utility\selenium_webdriver\selenium_log.py
# C:\Users\OK\source\repos\Repository4_python\scraping_test\selenium_utility\google_search_info.py
import sys
path = r'C:\Users\OK\source\repos\Repository4_python\scraping_test'
sys.path.append(path)
from html_log.html_logger import LogLevel
#/
class SeleniumLogger():
    def __init__(self,log_dir:str='',any_logger=None) -> None:
        if log_dir == '':
            path = str(pathlib.Path(__file__).parent.parent.joinpath('log'))
            log_dir = path
        self.set_log_dir(log_dir)
        self.log_file_path = os.path.join(self.log_dir,'log.txt')
        self.screenshot_dir_name = 'screenshot'
        self.logger = any_logger
    def set_log_dir(self,dir:str,screenshot_dir_name:str='screenshot'):
        import os
        if not os.path.exists(dir):
            os.mkdir(dir)
        else:
            if os.path.isfile(dir):
                os.remove(dir)
                os.mkdir(dir)
        self.log_dir = dir
        self.screenshot_dir = os.path.join(self.log_dir,screenshot_dir_name)
    def __get_time(self):
        return datetime.datetime.now().strftime('%Y/%M/%D %h:%m:%d:%s.%f') + '  '
    def __write_file(self,value):
        with open(self.log_file_path,'a',encoding='utf-8')as f:
            f.write(value)
    def add_log(self,value:str,log_level:int=LogLevel.INFO.value):
        value = self.__get_time + value
        print(value)
        self.__write_file(value + '\n')
    def add_log_sepalater(self):
        bar = '============================================='
        self.add_log(bar)



from html_log.html_logger import BasicLogger
class SeleniumBasicLogger(BasicLogger):
    """
    class BasicLogger(metaclass=ABCMeta)
        Inherit:BasicLogger
         ..\common_utility\log_util\logging_util.py
    """

    ######### Selenium 共通
    # HTML、BasicなどそれぞれLoggerの構成が異なるため、以下メソッドを別途用意
    def add_log_screenshot(self,image_path:str,screenshot_log:str,log_level:int=LogLevel.INFO):
        """
         == add_log_screenshot_copy
        """
        self.add_log_screenshot_copy(image_path,screenshot_log,log_level)
    def add_log_screenshot_move(self,image_path:str,screenshot_log:str,log_level:int=LogLevel.INFO):
        """
        イメージファイルをLogのディレクトリに移動して
         Log内容と移動したイメージファイルのパスをLogに追記する。
        """
        path = self._move(image_path, self.get_image_dir_path())
        self.add_log(screenshot_log,log_level)
        self.add_log(path,log_level)
    def add_log_screenshot_copy(self,image_path:str,screenshot_log:str,log_level:int=LogLevel.INFO):
        """
        イメージファイルをLogのディレクトリにコピーして
         Log内容とコピーしたイメージファイルのパスをLogに追記する。
        """
        path = self._copy(image_path, self.get_image_dir_path())
        self.add_log(screenshot_log,log_level)
        self.add_log(path,log_level)
    ##########

from html_log.html_logger import HtmlLogger
class SeleniumHtmlLogger(SeleniumBasicLogger):
    """

    Inherit:SeleniumBasicLogger(BasicLogger)
     selenium_log.py
    """
    # def __init__(
    #     self, 
    #     log_dir: str,
    #     log_dir_name: str = 'log',
    #     log_file_name: str = 'log.txt',
    #     log_image_dir_name: str = 'log_image') -> None:
    #     super().__init__(log_dir, log_dir_name, log_file_name, log_image_dir_name)
    def __init__(self, html_logger:HtmlLogger) -> None:
        self.log_dir = html_logger.logger_dir_path
        log_dir = self.log_dir
        log_dir_name = html_logger.log_dir_name
        log_file_name = html_logger.log_txt_file_name
        log_image_dir_name = html_logger.log_image_dir_name
        super().__init__(log_dir, log_dir_name, log_file_name, log_image_dir_name)
        self.set_html_logger(html_logger)
    def set_html_logger(self,html_logger:HtmlLogger):
        self.html_logger = html_logger
    def add_log(self,value:str,log_level:int=LogLevel.INFO.value):
        self.html_logger.add_log(value)
    def add_log_sepalater(self):
        bar = '============================================='
        self.html_logger.add_log(bar)
    ######### Selenium 共通
    # HTML、BasicなどそれぞれLoggerの攻勢が異なるため、以下メソッドを別途用意
    def add_log_screenshot(self, image_path: str, screenshot_log: str, log_level: int = LogLevel.INFO):
        super().add_log_screenshot(image_path,screenshot_log,log_level)
        self.html_logger.add_log_image(image_path,screenshot_log)
        # return super().add_log_screenshot(image_path, screenshot_log, log_level)
    # def add_log_screenshot(self,image_path:str,screenshot_log:str,log_level:int=LogLevel.INFO):
    #     self.add_log_screenshot_move(image_path,screenshot_log,log_level)
    #     self.html_logger
    # def add_log_screenshot_move(self,image_path:str,screenshot_log:str,log_level:int=LogLevel.INFO):
    #     """
    #     イメージファイルをLogのディレクトリに移動して
    #      Log内容と移動したイメージファイルのパスをLogに追記する。
    #     """
    #     path = self._move(image_path, self.image_dir)
    #     self.add_log(self,screenshot_log,log_level)
    #     self.add_log(self,path,log_level)
    # def add_log_screenshot_copy(self,image_path:str,screenshot_log:str,log_level:int=LogLevel.INFO):
    #     """
    #     イメージファイルをLogのディレクトリにコピーして
    #      Log内容とコピーしたイメージファイルのパスをLogに追記する。
    #     """
    #     path = self._copy(image_path, self.image_dir)
    #     self.add_log(self,screenshot_log,log_level)
    #     self.add_log(self,path,log_level)
    # ##########

def get_selenium_logger(logger):
    if isinstance(logger,BasicLogger):
        logger.__class__ = SeleniumBasicLogger
        ret_logger = logger
    elif isinstance(logger,HtmlLogger):
        ret_logger = SeleniumHtmlLogger(logger)
    else:
        ret_logger = SeleniumLogger(logger.log_file_path,logger)
    return ret_logger



import os
import sys
from selenium.webdriver.chrome.options import Options

from selenium import webdriver
def screenshot(driver:webdriver.Chrome,image_file_path:str):

    # File Name
    # FILENAME = os.path.join(os.path.dirname(os.path.abspath(__file__)), "image/screen.png")

    # set driver and url
    # driver = webdriver.Chrome('./chromedriver')
    # url = 'https://www.rakuten.co.jp/'
    # driver.get(url)

    # get width and height of the page
    w = driver.execute_script("return document.body.scrollWidth;")
    h = driver.execute_script("return document.body.scrollHeight;")
    # set window size
    driver.set_window_size(w,h)
    # Get Screen Shot
    driver.save_screenshot(image_file_path)

    # Close Web Browser
    # driver.quit()