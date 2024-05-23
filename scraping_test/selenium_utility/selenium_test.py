

from search_info import AbstractSearchInfomations,TaargetDataInfo
from pathlib import Path



from selenium.webdriver.common.by import By
from selenium_webdriver.webdriver_utility import WebDriverUtility
from selenium_utility.selenium_webdriver.selenium_log import SeleniumBasicLogger

class TestWebDriverUtility():
    """WebDriverUtilityをテストする"""

    def __init__(self,target_data_info:TaargetDataInfo,web_driver_path:str) -> None:
        self.target:TaargetDataInfo = target_data_info
        self.web_deiver_path = web_driver_path
        self.log_dir = ''
        self.image_dir = ''
    
    def set_log_dir(self,dir:str):
        import os
        if not os.path.exists(dir):
            os.mkdir(dir)
        else:
            if os.path.isfile(dir):
                os.remove(dir)
                os.mkdir(dir)
        self.log_dir = dir
    
    def prepare_data(self):
        pass

    def run_app(self, logger, target_url:str):
        self.chrome = WebDriverUtility(self.web_deiver_path, logger)
        self.chrome.image_dir = self.image_dir
        self.chrome.driver.get(target_url)
        logger:SeleniumBasicLogger = logger
        self.chrome.selenium_log.set_log_dir(self.log_dir, Path(logger.image_dir_path).name)

    def test_method(self):
        self.chrome.find_element
        # #####
        # # 画像検索をして、clickする
        # image_path = self.chrome.save_page_source_and_screenshot()
        # self.chrome.selenium_log.add_log('image_path = {}'.format(image_path))
        # # C:\Users\OK\source\repos\Repository4_python\scraping_test\selenium_utility\selenium_test.py
        # image_dir = Path(__file__).parent.joinpath('image/__img_selenium_test')
        # temp_img_file_name = 'youtube_logo_small.jpg'
        # templete_image_path = image_dir.joinpath(temp_img_file_name)
        # # rect={'height': 5, 'width': 840, 'x': 36, 'y': 514}
        # rect = self.chrome.find_image(
        #     image_path, templete_image_path)
        # self.chrome.draw_rect(image_path, rect)
        # x,y = self.chrome.get_rect_center(rect)
        # self.chrome.click_point(x,y)
        # #####
        image_dir = Path(__file__).parent.joinpath('image/__img_selenium_test')
        temp_img_file_name = 'youtube_logo_small.jpg'
        templete_image_path = image_dir.joinpath(temp_img_file_name)
        self.chrome.click_by_image(templete_image_path)



    def trandition_input_screen(self):
        pass

    def input_data(self):
        # search_bar = self.chrome.driver.find_element_by_name("q")
        # AttributeError: 'WebDriver' object has no attribute 'find_element_by_name'
        search_bar = self.chrome.driver.find_element('name', 'q')
        search_bar.send_keys(self.target.data_value)
        search_bar.submit()

    def get_result(self):
        self.chrome.screenshot()
        self.chrome.write_page_source()
        # elements = self.chrome.driver.find_elements_by_xpath('//a/h3')
        elements = self.chrome.driver.find_elements(By.XPATH, '//a/h3')
        for elem_h3 in elements:
            # elem_a = elem_h3.find_element_by_xpath('..')
            elem_a = elem_h3.find_element(By.XPATH, '..')
            print(elem_h3.text)
            print(elem_a.get_attribute('href'))
        
    def align_result(self):
        pass
    
    def analyze_result(self):
        pass

    def determine_if_values_match(self):
        """値が一致しているか判定する determine if the values match"""
        pass


def test_main():
    target_data = TaargetDataInfo('python')
    CHROME_DRIVER_PAT = r'C:\Users\OK\source\programs\chromedriver_win32\chromedriver'
    
    # GOOGLE_URL = 'https://www.google.co.jp/'
    TARGET_URL = 'https://www.youtube.com/results?search_query=%E4%B8%80%E7%99%BD%E6%B0%B4%E6%98%9F'
    #/
    driver_util = TestWebDriverUtility(target_data, CHROME_DRIVER_PAT)
    #/
    import datetime
    datetime_str = datetime.datetime.now().strftime('%y%m%d_%H%M%S')
    log_dir = Path(__file__).parent.joinpath('log/__log_' + datetime_str)
    from selenium_utility.selenium_webdriver.selenium_log import SeleniumLogger
    from selenium_utility.selenium_webdriver.selenium_log import SeleniumBasicLogger
    # logger = SeleniumLogger(log_dir=log_dir)
    logger = SeleniumBasicLogger(log_dir=log_dir)
    # logger.set_log_dir()
    log_dir.mkdir(exist_ok=True)
    # google_searcher.set_log_dir(str(Path(__file__).parent.joinpath('log')))
    #/
    driver_util.set_log_dir(log_dir)
    path = Path(__file__).parent.joinpath('image/__img_selenium_test')
    driver_util.image_dir = path
    driver_util.run_app(logger, TARGET_URL)
    #####
    # add_logの時にコンソールに出力するために、コンソール用のログレベルをセットする
    # LogLever定数クラスを使うためにlog_utilをsys.appendしている
    #/
    #memo
    # C:\Users\OK\source\repos\Repository4_python\scraping_test\selenium_utility\selenium_test.py
    # C:\Users\OK\source\repos\Repository4_python\common_utility\log_util\logging_util.py
    #/
    append_path = str(Path(__file__).parent.parent.parent) # Repository4_python
    append_path = str(Path(append_path).joinpath('common_utility\log_util'))
    import sys
    sys.path.append(append_path)
    from logging_util import LogLevel
    driver_util.chrome.selenium_log.log_level_console = LogLevel.INFO.value
    ###
    msg = 'logger_class = {}'.format(driver_util.chrome.selenium_log.__class__)
    driver_util.chrome.selenium_log.add_log(msg)
    print(msg)
    #####
    driver_util.test_method()
    # driver_util.input_data()
    # driver_util.get_result()
    import time
    time.sleep(2)
    driver_util.chrome.close()
    msg = 'selenium_log_path = {}'.format(driver_util.chrome.selenium_log.log_dir)
    driver_util.chrome.selenium_log.add_log(msg)
    print(msg)
    msg = 'log_path = {}'.format(logger.log_dir)
    driver_util.chrome.selenium_log.add_log(msg)
    print(msg)

if __name__ == '__main__':
    test_main()