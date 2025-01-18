from fileinput import filename
from inspect import trace
from import_init import selenium_utility
# from import_init import WebDriverUtility

from selenium_utility import selenium_webdriver
from selenium_utility.selenium_webdriver.webdriver_utility import WebDriverUtility
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webdriver import WebElement
from html_log.html_logger import HtmlLogger as WdLogger
import os
from selenium.webdriver.common.by import By

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
        el = self.chrome.driver.find_element(By.CLASS_NAME, value)
        self.chrome.timer.wait()
        msg = 'send file path = {}'.format(path)
        self.logger.add_log(msg)
        ss_path = self.chrome.screenshot()
        self.logger.add_log_image(
            ss_path,css_add_class_name=IMAGE_TAG_EDGE_GRAY)
        # 送信ボタンをクリック
        el.send_keys(path)
        self.chrome.timer.wait()
        self.logger.add_log('after select file')
        ss_path = self.chrome.screenshot()
        self.logger.add_log_image(
            ss_path,css_add_class_name=IMAGE_TAG_EDGE_GRAY)

        value = 'styled'
        el = self.chrome.driver.find_element(By.CLASS_NAME, value)
        el.click()
        self.chrome.timer.wait()
        # search_bar = self.chrome.driver.find_element_by_name("q")
        # search_bar.send_keys(self.target.data_value)
        # search_bar.submit()

    def get_result(self):
        ss_path = self.chrome.screenshot()
        self.chrome.write_page_source()
        self.logger.add_log('after click send button')
        self.logger.add_log_image(
            ss_path,css_add_class_name=IMAGE_TAG_EDGE_GRAY)
        # for elem_h3 in self.chrome.driver.find_elements_by_xpath('//a/h3'):
        #     elem_a = elem_h3.find_element_by_xpath('..')
        #     print(elem_h3.text)
        #     print(elem_a.get_attribute('href'))
        
    def align_result(self):
        pass
    
    def analyze_result(self):
        pass


    def analyze_web(self):
        
        element:WebElement=None
        from selenium.webdriver.common.action_chains import ActionChains

        driver = self.chrome.driver
        from selenium.webdriver.common.keys import Keys
        import time
        count = 300
        print('\n********')
        msg = 'YouTube_Warning_AdSence'
        self.chrome.save_page_source_and_screenshot_with_log(msg)
        for i in range(count):
            time.sleep(0.25)
            element = driver.switch_to.active_element
            classname = element.get_attribute('class')
            tagname = element.get_attribute('innerHTML')
            print('\n{}: '.format(i))
            # print('    {}'.format(classname))
            # print('    {}'.format(tagname))
            self.print_element(element)
            if classname == 'text-decoration-none ac-btn-md ac-btn-photo w-100 justify-content-center custom-shadow historyDowloads':
                element.click()
            
            # ElementNotInteractableException
            # Message: element not interactable
            try:
                element.send_keys(Keys.TAB)
            except:
                print()
                print('----------')
                import traceback
                traceback.print_exc()
                break

        print()
        # source = driver.page_source
        # with open('souce.txt','w',encoding='utf-8')as f:
        #     f.write(source)

        # xpath = "//*[@text='ダウンロード']"
        # xpath = "//*[@class='text-decoration-none']"
        # el = driver.find_element_by_xpath(xpath)
        # el.click()
        
        # class_name = 'text-decoration-none ac-btn-md ac-btn-photo w-100 justify-content-center custom-shadow historyDowloads'
        # el = driver.find_element(By.CLASS_NAME, class_name)
        # el.click()

    def print_element(self,element:WebElement):
        attribute_names = [
            'class','value','id'
        ]
        print('*******')
        print('    {}={}'.format('tag_name', element.tag_name))
        buf = element.get_attribute('innerHTML')
        if len(buf)>10: buf = buf[:10]
        print('    {}={}'.format('innerHTML[10]', buf))
        buf = str(element.rect)
        print('    {}={}'.format('rect', buf))
        for attr_name in attribute_names:
            buf = self.chrome.get_webelement_attribute(element,attr_name)
            print('    {}={}'.format(attr_name, buf))

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
    target_url = '//127.0.0.1:5000/submit_top'
    target_url = 'https://www.youtube.com/watch?v=00AAAo4AAa0'

    log_dir_path = str(pathlib.Path(__file__).parent.joinpath('log'))
    log_dir_name = get_log_dir_name()
    from html_log.html_logger import HtmlLogger
    html_logger = HtmlLogger('FlaskTest2',log_dir_path, log_dir_name)
    # html_logger.set_css_path('log.css')
    copy_css(html_logger.logger_dir_path, html_logger.html_writer.css_path)
    html_logger.create_log()
    fd = TestFlaskDriver(target_url, wd_path)
    fd.set_logger(html_logger)
    fd.run_app()

    # fd.input_data()
    fd.analyze_web()
    fd.get_result()
    fd.chrome.timer.wait_longer()
    fd.logger.finish_to_create_html()
    fd.chrome.close()

if __name__ == '__main__':
    test_main()