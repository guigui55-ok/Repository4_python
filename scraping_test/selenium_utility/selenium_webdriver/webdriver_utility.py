"""

https://ai-inter1.com/python-selenium/


例外が発生しました: SessionNotCreatedException
Message: session not created: This version of ChromeDriver only supports Chrome version 94
Current browser version is 101.0.4951.67 with binary path C:\Program Files 
→バージョンがインストールされているブラウザ版と違う

https://yuki.world/python-chrome-driver-version-error/
pip install chromedriver-binary

pip install chromedriver-binary==79.0.3945.36.0
ChromeDriver 102.0.5005.61

pip install chromedriver-binary==102.0.5005.61
"""
from selenium import webdriver
import os


# from selenium_utility.selenium_webdriver.selenium_log import SeleniumLogger
# from selenium_utility.selenium_webdriver.selenium_log import SeleniumLogger
from selenium_webdriver.selenium_log import SeleniumLogger

class BrowserKind():
    CHROME = 1
    EDGE = 2
    FIREFOX = 3

class WebDriverUtility():
    def __init__(self,webdriver_path:str) -> None:
        if not os.path.exists:
            raise Exception('path not exists. [path={}]'.format(webdriver_path))
        self.driver = webdriver.Chrome(webdriver_path)
        self.selenium_log = SeleniumLogger()
    
    def close(self):
        self.driver.close()
        self.driver.quit()

    def write_page_source(self,file_path:str=''):
        driver = self.driver
        import os
        if file_path=='':
            file_path = self.selenium_log.log_dir
        if os.path.exists(file_path) and os.path.isfile(file_path):
            os.remove(file_path)
            os.mkdir(file_path)
        if os.path.isdir(file_path):
                import datetime
                file_name = datetime.datetime.now().strftime('%Y%m%d_%H%M%S') + '_chrome_source.html'
                file_path = os.path.join(file_path,file_name)
        data = driver.page_source
        with open(file_path,'w',encoding='utf-8')as f:
            f.write(data)

    def screenshot(self,image_file_path:str=''):
        driver = self.driver
        import os
        if image_file_path=='':
            image_file_path = self.selenium_log.log_dir
        if os.path.exists(image_file_path) and os.path.isfile(image_file_path):
            os.remove(image_file_path)
            os.mkdir(image_file_path)
        if os.path.isdir(image_file_path):
                import datetime
                file_name = datetime.datetime.now().strftime('%Y%m%d_%H%M%S') + '_chrome.png'
                image_file_path = os.path.join(image_file_path,file_name)
        print('screenshot = {}'.format(image_file_path))
        # get width and height of the page
        w = driver.execute_script("return document.body.scrollWidth;")
        h = driver.execute_script("return document.body.scrollHeight;")
        # set window size
        driver.set_window_size(w,h)
        # Get Screen Shot
        driver.save_screenshot(image_file_path)