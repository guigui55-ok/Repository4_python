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
from webbrowser import Chrome
from selenium import webdriver
import os
import traceback

# from selenium_utility.selenium_webdriver.selenium_log import SeleniumLogger
# from selenium_utility.selenium_webdriver.selenium_log import SeleniumLogger
if __name__ == '__main__':
    from selenium_log import SeleniumLogger
else:
    from selenium_webdriver.selenium_log import SeleniumLogger
    from selenium_webdriver.general import Waiter
    import selenium_webdriver.selenium_const as selenium_const

class BrowserKind():
    CHROME = 1
    EDGE = 2
    FIREFOX = 3

class MatchType():
    ALL = 1
    PART = 2
    START_WITH = 3
    END_WITH = 4
    REGULAR_EXPRESSIONS = 5

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webdriver import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.common import keys


class WebElementUtility():
    def __init__(self,element:WebElement) -> None:
         self.element = element
         self.util:WebElementGeneral = WebElementGeneral(element)
        
    def set_find_value(self,value:str,by:By):
        self.value = value
        self.by = by
        
    def print_attributes(self,attr_name_list:'list[str]'=['text']):
        for attr_name in attr_name_list:
            buf = self.get_attribute(attr_name)
            print(buf)
    
    def get_attribute(self,attr_name:str):
        try:
            if self.element == None:
                return 'NONE'
            return str(self.element.get_attribute(attr_name))
        except Exception as e:
            print(str(e))
            return ''

class WebElementGeneral():
    def __init__(self,element:WebElement) -> None:
         self.element = element
    def get_text(self):
        return WebElementUtility(self.element).get_attribute('text')
    def get_value(self):
        return WebElementUtility(self.element).get_attribute('value')
    def get_class(self):
        return WebElementUtility(self.element).get_attribute('class')

import re
class PageSourceUtility():
    def __init__(self,webdriver=None) -> None:
        self.webdriver:WebDriver = webdriver
        self.page_source = ''
        self.is_with_update=True
    def update_page_source_with_flag(self,is_update:bool=None):
        if is_update==None: is_update=self.is_with_update
        if is_update:
            self.update_page_source()
    def update_page_source(self):
        self.page_source = self.webdriver.page_source
    def is_exists_find_all(self,value:str,is_update:bool=None):
        self.update_page_source_with_flag(is_update)
        try:
            pos = self.page_source.find(value)
            if pos>=0:
                return True
            return False
        except:
            traceback.print_exc()
            return False

    def find_all_re(self,pattern:str):
        self.update_page_source_with_flag()
        result = re.findall(pattern,self.page_source)
        return result

class WebDriverUtility():
    def __init__(self,webdriver_path:str) -> None:
        if not os.path.exists:
            raise Exception('path not exists. [path={}]'.format(webdriver_path))
        if webdriver_path != '':
            self.driver = webdriver.Chrome(webdriver_path)
        else:
            self.driver:webdriver.Chrome=None
        self.selenium_log = SeleniumLogger()
        self.page_source_ex = PageSourceUtility(self.driver)
        self.timer:Waiter = Waiter(selenium_const.DEFAULT_WAIT_TIME)
    
    def get_webelement_attribute(self,element:WebElement,attr_name:str):
        if element==None:
            return 'None'
        return WebElementUtility(element).get_attribute(attr_name)

    def close(self):
        self.driver.close()
        self.driver.quit()
    

    def save_page_source_and_screenshot(self,add_str:str='',dir_path:str=''):
        ext='_chrome_image.png'
        image_path = self.get_save_path(base_name='', add_str=add_str, ext=ext, dir_path=dir_path)
        self.screenshot(image_path)
        ext='_chrome_source.html.txt'
        source_path = self.get_save_path(base_name='', add_str=add_str, ext=ext, dir_path=dir_path)
        self.write_page_source(source_path)
        print()
        print()
        print('*****')
        print('save_page_source_and_screenshot')
        print('source = {}'.format(source_path))
        print('image = {}'.format(image_path))
        print()
    
    def get_save_file_name(self,base_name:str='',add_str:str='',ext:str=''):
        if ext=='': ext='.txt'
        if base_name=='':
            import datetime
            file_name = datetime.datetime.now().strftime('%Y%m%d_%H%M%S') + add_str + ext
        else:
            file_name = base_name + add_str + ext
        return file_name

    def get_save_path(self,base_name:str='', add_str:str='', ext:str='', dir_path:str=''):
        """
        空ならlog_dirにyymmdd_hhmmss_chrome_source.htmlとして保存する
         log_dirが設定されているが、ない場合、
         　　ファイルであれば削除してdirを作成
         　　dirがなければ作成

        """
        import os
        if dir_path=='':
            dir_path = self.selenium_log.log_dir
        if os.path.exists(dir_path) and os.path.isfile(dir_path):
            os.remove(dir_path)
            os.mkdir(dir_path)
        if not os.path.exists( os.path.dirname(dir_path) ):
            os.mkdir(dir_path)
        if os.path.isdir(dir_path):
            file_name = self.get_save_file_name(base_name,add_str,ext)
            file_path = os.path.join(dir_path,file_name)
        return file_path

    def write_page_source(self,file_path:str=''):
        driver = self.driver
        if file_path=='':
            file_path = self.get_save_path('_chrome_source.html')
        data = driver.page_source
        with open(file_path,'w',encoding='utf-8')as f:
            f.write(data)

    def screenshot(self,image_file_path:str=''):
        driver = self.driver
        if image_file_path=='':
            image_file_path = self.get_save_path('_chrome.png')
        print('screenshot = {}'.format(image_file_path))
        # get width and height of the page
        w = driver.execute_script("return document.body.scrollWidth;")
        h = driver.execute_script("return document.body.scrollHeight;")
        # set window size
        driver.set_window_size(w,h)
        # Get Screen Shot
        driver.save_screenshot(image_file_path)
        return image_file_path

    
    def get_element():
        pass