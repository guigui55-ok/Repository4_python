from fileinput import filename
from import_init import selenium_utility
# from import_init import WebDriverUtility

from selenium_utility import selenium_webdriver
from selenium_utility.selenium_webdriver.webdriver_utility import WebDriverUtility
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webdriver import WebElement
from html_log.html_logger import HtmlLogger as WdLogger
import os

IMAGE_TAG_EDGE_GRAY = 'log-image-gray-edge'

class TestFlaskDriver():
    """TestFlaskのWebSiteを操作する"""

    def __init__(self,target_url,web_driver_path:str) -> None:
        self.target_url = target_url
        self.web_deiver_path = web_driver_path
        self.log_dir = ''
        self.chrome = None
        self.logger:WdLogger = None

    def set_logger(self,logger:WdLogger):
        self.set_log_dir(logger.logger_dir_path)
        self.logger = logger
        if self.chrome!=None:
            self.chrome.set_logger(logger)
    
    def set_log_dir(self,dir:str):
        self.log_dir = dir
        if not os.path.exists(dir):
            os.mkdir(dir)
    
    def prepare_data(self):
        pass

    def run_app(self):
        self.chrome = WebDriverUtility(self.web_deiver_path, self.logger)
        msg = 'self.chrome.driver.get  url={}'.format(self.target_url)
        self.logger.add_log(msg)
        self.chrome.driver.get(self.target_url)
        self.chrome.selenium_log.set_log_dir(self.log_dir, self.logger.log_image_dir_name)

    def trandition_to_input_screen(self):
        pass

    def input_data(self):
        # 送信するファイルをセット
        import pathlib
        file_name = 'send_test.txt'
        path = str(pathlib.Path(__file__).parent.joinpath(file_name))
        # ファイルを選択するボタンを取得して、ファイルパスを入力
        value = 'select-file-button'
        el = self.chrome.driver.find_element_by_class_name(value)
        self.chrome.timer.wait()
        msg = 'send file path = {}'.format(path)
        self.logger.add_log(msg)
        ss_path = self.chrome.screenshot()
        self.logger.add_log_image(
            ss_path,css_add_class_name=IMAGE_TAG_EDGE_GRAY)
        # 送信ボタンをクリック
        el.send_keys(path)
        self.chrome.timer.wait()
        self.logger.add_log('click send button')
        ss_path = self.chrome.screenshot()
        self.logger.add_log_image(
            ss_path,css_add_class_name=IMAGE_TAG_EDGE_GRAY)

        value = 'styled'
        el = self.chrome.driver.find_element_by_class_name(value)
        el.click()
        self.chrome.timer.wait()
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

import pathlib,os
def copy_css(dist_dir, dist_file_name):
    import shutil
    file_name='log.css'
    src_path = str(pathlib.Path(__file__).parent.joinpath(file_name))
    dist_path = os.path.join(dist_dir,dist_file_name)
    shutil.copy(src_path, dist_path)

def get_log_dir_name(base_name:str='log_'):
    import datetime
    date = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
    return base_name + date



def test_main():
    wd_path = r'C:\Users\OK\source\programs\chromedriver_win32\chromedriver'

    target_url = 'http://192.168.1.9:5000/temp'
    target_url = 'http://127.0.0.1:5000/submit_top'
    target_url = 'https://www.photo-ac.com/main/detail/24553230'

    log_dir_path = str(pathlib.Path(__file__).parent.joinpath('log'))
    log_dir_name = get_log_dir_name()
    from html_log.html_logger import HtmlLogger
    html_logger = HtmlLogger('FlaskTest2',log_dir_path, log_dir_name)
    html_logger.set_css_path('log.css')
    copy_css(html_logger.logger_dir_path, html_logger.html_writer.css_path)
    html_logger.create_log()
    # html_logger.log_image_dir_name
    fd = TestFlaskDriver(target_url, wd_path)
    # fd.logger = html_logger
    # fd.set_log_dir(str(pathlib.Path(__file__).parent.joinpath('log')))
    fd.set_logger(html_logger)
    fd.run_app()

    element:WebElement=None
    from selenium.webdriver.common.action_chains import ActionChains
    def click_position(driver:WebDriver ,x, y) -> None:
        actions = ActionChains(driver)
        html_element = driver.find_element_by_tag_name("html")
        actions.move_to_element_with_offset(html_element, 0, 0)
        actions.move_by_offset(x, y)
        actions.click()
        actions.perform()

    driver = fd.chrome.driver
    from selenium.webdriver.common.keys import Keys
    import time
    count = 100
    for i in range(count):
        time.sleep(0.25)
        element = driver.switch_to.active_element
        value = element.get_attribute('class')
        if value == 'text-decoration-none ac-btn-md ac-btn-photo w-100 justify-content-center custom-shadow historyDowloads':
            element.click()
        element.send_keys(Keys.TAB)

    print()
    # source = driver.page_source
    # with open('souce.txt','w',encoding='utf-8')as f:
    #     f.write(source)

    xpath = "//*[@text='ダウンロード']"
    xpath = "//*[@class='text-decoration-none']"
    el = driver.find_element_by_xpath(xpath)
    el.click()
    
    class_name = 'text-decoration-none ac-btn-md ac-btn-photo w-100 justify-content-center custom-shadow historyDowloads'
    el = driver.find_element_by_class_name(class_name)
    el.click()
#例外が発生しました: NoSuchElementException
#Message: no such element: Unable to locate element: {"method":"css selector","selector":".text-decoration-none ac-btn-md ac-btn-photo w-100 justify-content-center custom-shadow historyDowloads"}
#  (Session info: chrome=105.0.5195.126)


# text-decoration-none ac-btn-md ac-btn-photo w-100 justify-content-center custom-shadow historyDowloads

    fd.input_data()
    fd.get_result()
    fd.chrome.timer.wait_longer()
    fd.logger.finish_to_create_html()
    fd.chrome.close()

if __name__ == '__main__':
    test_main()