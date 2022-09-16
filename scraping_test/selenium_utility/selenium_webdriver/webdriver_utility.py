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
from cgitb import html
from string import hexdigits
from turtle import width
from webbrowser import Chrome
from selenium import webdriver
import os
import traceback

from sympy import cxxcode

# from selenium_utility.selenium_webdriver.selenium_log import SeleniumLogger
# from selenium_utility.selenium_webdriver.selenium_log import SeleniumLogger
if __name__ == '__main__':
    from selenium_log import SeleniumLogger,get_selenium_logger
else:
    from selenium_webdriver.selenium_log import SeleniumLogger,get_selenium_logger
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

from selenium.webdriver.common.action_chains import ActionChains


class WebElementUtility():
    def __init__(self,element:WebElement) -> None:
        self.element = element
        self.util:WebElementGeneral = WebElementGeneral(element)
        self.none_is_error = False
        
    def set_find_value(self,value:str,by:By):
        self.value = value
        self.by = by
    
    def print_attributes_for_analyze(self):
        """
        ['text','class','id','value']
        """
        attr_names = ['text','class','id','value']
        self.print_attributes(attr_names)
        
    def print_attributes(self,attr_name_list:'list[str]'=['text']):
        for i in range(len(attr_name_list)):
            attr_name = attr_name_list[i]
            buf = self.get_attribute(attr_name)
            msg = '{}={}'.format(attr_name,buf)
            print(msg)
            if i != len(attr_name_list)-1:
                print(' , ')
    
    def get_attribute(self,attr_name:str):
        try:
            if self.element == None:
                return 'NONE'
            return str(self.element.get_attribute(attr_name))
        except Exception as e:
            print(str(e))
            return ''
    
    def get_center_position(self):
        x,y = self.get_position()
        width ,height = self.get_size()
        c_x = x + (width//2)
        c_y = y + (height//2)
        return c_x,c_y
    def get_rect(self):
        if self.__is_none(): return
        x,y = self.get_position()
        width ,height = self.get_size()
        return [[x,y],[width,height]]
    def get_size(self):
        width = self.element.size['width']
        height = self.element.size['height']
        return width,height
    def get_position(self):
        x = self.element.location['x']
        y = self.element.location['y']
        return x,y
    
    def __is_none(self):
        if self.element==None:
            raise Exception('self.element is None.')
        return False

class WebElementGeneral():
    def __init__(self,element:WebElement) -> None:
         self.element = element
    def get_text(self):
        return WebElementUtility(self.element).get_attribute('text')
    def get_value(self):
        return WebElementUtility(self.element).get_attribute('value')
    def get_class(self):
        return WebElementUtility(self.element).get_attribute('class')
    def get_position(self):
        return WebElementUtility(self.element).get_position()

import re
class PageSourceUtility():
    def __init__(self,webdriver=None) -> None:
        self.webdriver:WebDriver = webdriver
        self.page_source = ''
        self.is_with_update=True
    def update_page_source_with_flag(self,is_update:bool=None):
        """
        フラグによって self.page_source を更新する
        """
        if is_update==None: is_update=self.is_with_update
        if is_update:
            self.update_page_source()
    def update_page_source(self):
        """
        self.page_source を更新する
        """
        self.page_source = self.webdriver.page_source
    def is_exists_find_all(self,value:str,is_update:bool=None):
        """
        self.page_source の中に文言が含まれるか判定する
         フラグによって page_source を更新する
        """
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
    def __init__(self,webdriver_path:str,logger) -> None:
        if webdriver_path != '':
            if not os.path.exists:
                raise Exception('path not exists. [path={}]'.format(webdriver_path))
            self.driver = webdriver.Chrome(webdriver_path)
            self.page_source_ex = PageSourceUtility(self.driver)
        else:
            self.driver:webdriver.Chrome=None
            self.page_source_ex  = None
        self.webdriver_path = webdriver_path
        # self.selenium_log = SeleniumLogger()
        self.selenium_log = get_selenium_logger(logger)
        self.timer:Waiter = Waiter(selenium_const.DEFAULT_WAIT_TIME)
        self.options:webdriver.ChromeOptions = None
    
        # self.selenium_log.add_log('')
    def set_driver(self,webdriver_path:str):
        self.driver:webdriver.Chrome=None
        self.page_source_ex  = None
        if not os.path.exists:
            raise Exception('path not exists. [path={}]'.format(webdriver_path))
        self.driver = webdriver.Chrome(webdriver_path,options=self.options)
        self.page_source_ex = PageSourceUtility(self.driver)


    def get_webelement_attribute(self,element:WebElement,attr_name:str):
        if element==None:
            return 'None'
        return WebElementUtility(element).get_attribute(attr_name)

    def close(self):
        """ driver.close -> driver.quit"""
        self.driver.close()
        self.driver.quit()
    
    def click_by_position(self,x, y) -> None:
        # from selenium.webdriver.common.action_chains import ActionChains
        actions = ActionChains(self.driver)

        # MOVE TO TOP_LEFT (`move_to_element` will guide you to the CENTER of the element)
        whole_page = self.driver.find_element_by_tag_name("html")
        # whole_page = self.driver.find_element_by_tag_name("body")
        rect = WebElementUtility(whole_page).get_rect()
        print(rect)
        actions.move_to_element_with_offset(whole_page, 0, 0)

        # MOVE TO DESIRED POSITION THEN CLICK
        actions.move_by_offset(x, y)
        actions.click()

        actions.perform()

    def click_by_position_(self,x,y):
        actions = ActionChains(self.driver)
        # el = self.driver.find_element_by_tag_name('body')
        el = self.driver.find_element_by_tag_name('html')
        rect = WebElementUtility(el).get_rect()
        print(rect)
        actions.move_to_element_with_offset(el, x, y).click().perform()
    
    def open_new_tab(self,url:str):
        
        # 新しいタブを作成する
        self.driver.execute_script("window.open();")
        # 新しいタブに切り替える
        self.driver.switch_to.window(self.driver.window_handles[1])
        # 新しいタブでURLアクセス
        self.driver.get(url)
    
    def change_before_tab(self):
        #前のタブに切り替え
        self.driver.switch_to.window(self.driver.window_handles[0])

    def change_tab(self,num):
        #前のタブに切り替え
        self.driver.switch_to.window(self.driver.window_handles[num])
    
    def install_addon(self,extension_path:str):
        self.options = webdriver.ChromeOptions()
        self.options.add_argument(f'load-extension={extension_path}')
        
    def save_page_source_and_screenshot_with_log(self,add_str:str='',dir_path:str='',log_level:int=199):
        ext='_chrome_image.png'
        image_path = self.get_save_path(base_name='', add_str=add_str, ext=ext, dir_path=dir_path)
        self.screenshot(image_path)
        ext='_chrome_source.html.txt'
        source_path = self.get_save_path(base_name='', add_str=add_str, ext=ext, dir_path=dir_path)
        self.write_page_source(source_path)
        print()
        print()
        print('*****')
        if log_level < 199:
            self.selenium_log.add_log('save_page_source_and_screenshot',log_level=log_level)
            self.selenium_log.add_log('source = {}'.format(source_path),log_level=log_level)
            self.selenium_log.add_log_screenshot(image_path,'save_page_source_and_screenshot',log_level=log_level)
        else:
            print('save_page_source_and_screenshot')
            print('source = {}'.format(source_path))
            print('image = {}'.format(image_path))
        print()
    
    def save_page_source_and_screenshot(self,add_str:str='',dir_path:str='',):
        self.save_page_source_and_screenshot_with_log(add_str,dir_path, self.selenium_log.log_level)
        # ext='_chrome_image.png'
        # image_path = self.get_save_path(base_name='', add_str=add_str, ext=ext, dir_path=dir_path)
        # self.screenshot(image_path)
        # ext='_chrome_source.html.txt'
        # source_path = self.get_save_path(base_name='', add_str=add_str, ext=ext, dir_path=dir_path)
        # self.write_page_source(source_path)
        # print()
        # print()
        # print('*****')
        # print('save_page_source_and_screenshot')
        # print('source = {}'.format(source_path))
        # print('image = {}'.format(image_path))
        # print()
    
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
            image_file_path = self.get_save_path('','_chrome','.png')
        print('screenshot = {}'.format(image_file_path))
        # get width and height of the page
        # w = driver.execute_script("return document.body.scrollWidth;")
        # h = driver.execute_script("return document.body.scrollHeight;") # Windowがリサイズされる
        html_el = driver.find_element_by_tag_name('body')
        w = html_el.size['width']
        h = html_el.size['height']
        print('screenshot w,h ={},{}'.format(w,h))
        # set window size
        driver.set_window_size(w,h)
        # Get Screen Shot
        driver.save_screenshot(image_file_path)
        return image_file_path

    
    def get_element():
        pass