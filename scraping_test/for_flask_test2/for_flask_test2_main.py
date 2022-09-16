from import_init import selenium_utility
# from import_init import WebDriverUtility

from selenium_utility import selenium_webdriver
from selenium_utility.selenium_webdriver.webdriver_utility import WebDriverUtility
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webdriver import WebElement
from html_log.html_logger import HtmlLogger
import os

class TestFlaskDriver():
    """TestFlaskのWebSiteを操作する"""

    def __init__(self,target_url,web_driver_path:str) -> None:
        self.target_url = target_url
        self.web_deiver_path = web_driver_path
        self.log_dir = ''
        self.chrome = None
        self.logger:HtmlLogger = None
    
    def set_log_dir(self,dir:str):
        self.log_dir = dir
        if not os.path.exists(dir):
            os.mkdir(dir)
    
    def prepare_data(self):
        pass

    def run_app(self):
        self.chrome = WebDriverUtility(self.web_deiver_path, self.logger)
        self.chrome.driver.get(self.target_url)
        self.chrome.selenium_log.set_log_dir(self.log_dir, self.logger.log_image_dir_name)

    def trandition_to_input_screen(self):
        pass

    def input_data(self):
        pass
        # search_bar = self.chrome.driver.find_element_by_name("q")
        # search_bar.send_keys(self.target.data_value)
        # search_bar.submit()

    def get_result(self):
        self.chrome.screenshot()
        self.chrome.write_page_source()
        # for elem_h3 in self.chrome.driver.find_elements_by_xpath('//a/h3'):
        #     elem_a = elem_h3.find_element_by_xpath('..')
        #     print(elem_h3.text)
        #     print(elem_a.get_attribute('href'))
        
    def align_result(self):
        pass
    
    def analyze_result(self):
        pass

    def determine_if_values_match(self):
        """値が一致しているか判定する determine if the values match"""
        pass

import pathlib
def test_main():
    wd_path = r'C:\Users\OK\source\programs\chromedriver_win32\chromedriver'
    log_dir_path = str(pathlib.Path(__file__).parent)
    target_url = 'http://192.168.1.9:5000/'
    from html_log.html_logger import HtmlLogger
    html_logger = HtmlLogger('FlaskTest2',log_dir_path)
    html_logger.log_image_dir_name
    fd = TestFlaskDriver(target_url, wd_path)
    fd.logger = html_logger
    fd.set_log_dir(str(pathlib.Path(__file__).parent.joinpath('log')))
    fd.run_app()
    fd.input_data()
    fd.get_result()
    fd.chrome.timer.wait_longer()
    fd.chrome.close()

if __name__ == '__main__':
    test_main()