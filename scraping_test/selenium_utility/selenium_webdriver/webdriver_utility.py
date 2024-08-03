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

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common import exceptions as selenium_ex
#find_imageで使用
import cv2
import numpy as np
#/
from pathlib import Path
import shutil
#/
import urllib3
import urllib3.connection

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
            if attr_name=='text':
                return str(self.element.text)
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
            if not os.path.exists(str(webdriver_path)):
                raise Exception('path not exists. [path={}]'.format(webdriver_path))
            self.driver = webdriver.Chrome(webdriver_path)
            self.page_source_ex = PageSourceUtility(self.driver)
        else:
            self.driver:webdriver.Chrome=None
            self.page_source_ex  = None
        self.webdriver_path = webdriver_path
        self.set_logger(logger)
        # self.selenium_log = SeleniumLogger()
        self.timer:Waiter = Waiter(selenium_const.DEFAULT_WAIT_TIME)
        self.options:webdriver.ChromeOptions = None
        self.image_dir:Path = ''
    
        # self.selenium_log.add_log('')

    ##########
    # 240521 追加

    def find_element(self, by, value, multi:bool=False):
        element = None
        try:
            if multi:
                element = self.driver.find_elements(by, value)
            else:
                element = self.driver.find_element(by, value)
        except selenium_ex.NoSuchElementException as e:
            msg = str(e)
            self.selenium_log.add_log(msg)
            self.save_page_source_and_screenshot(msg)
            raise e
        return element

    def find_elements(self, by, value)->'list[WebElement]':
        return self.find_element(by, value, multi=True)
    
    def click(self, element:WebElement):
        try:
            element.click()
            self.selenium_log.add_log('clicked element')
        except selenium_ex.ElementClickInterceptedException as e:
            msg = str(e)
            self.selenium_log.add_log(msg)
            msg = 'selenium_ex.ElementClickInterceptedException'
            self.save_page_source_and_screenshot(msg)
            raise e
        return element

    def click_point(self, x, y):
        # ActionChainsを使用して座標を指定し、クリックを実行
        ActionChains(self.driver).move_by_offset(x, y).click().perform()
        # 次のアクションのためにマウスを元の位置に戻す
        ActionChains(self.driver).move_by_offset(-x, -y).perform()
        msg = 'click_point({},{})'.format(x,y)
        self.selenium_log.add_log(msg)

    def find_image(self,main_image_path, template_image_path, threshold=0.9):
        # 画像を読み込む
        main_image = cv2.imread(str(main_image_path))
        template_image = cv2.imread(str(template_image_path))
        # テンプレートマッチングを行う
        result = cv2.matchTemplate(main_image, template_image, cv2.TM_CCOEFF_NORMED)
        # 最も一致する位置を取得
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        self.selenium_log.add_log('max_val = {}'.format(max_val))
        # テンプレート画像の高さと幅
        template_height, template_width = template_image.shape[:2]
        # 最大一致度が閾値以上なら結果を返す、そうでない場合はゼロの座標とサイズを返す
        # 結果の辞書を作成
        if max_val >= threshold:
            rect = {
                'x': max_loc[0],
                'y': max_loc[1],
                'width': template_width,
                'height': template_height
            }
            self.selenium_log.add_log('Match Image True')
        else:
            rect = {
                'x': 0,
                'y': 0,
                'width': 0,
                'height': 0
            }
            self.selenium_log.add_log('Match Image False')
        msg = 'main image[{}]'.format(Path(main_image_path).name)
        self.selenium_log.add_log(msg)
        msg = 'temp image[{}]'.format(Path(template_image_path).name)
        self.selenium_log.add_log(msg)
        self.selenium_log.add_log('rect = {}'.format(str(rect)))
        return rect
    
    def rect_is_zero(self, rect):
        x = rect['x']
        y = rect['y']
        w = rect['width']
        h = rect['height']
        if x==0 and y==0 and w==0 and h==0:
            return True
        else:
            return False

    def get_rect_center(self, rect):
        x2 = rect['width']//2
        y2 = rect['height']//2
        center_x = rect['x'] + x2
        center_y = rect['y'] + y2
        return center_x, center_y

    def draw_rect(self, main_image_path, rect):
        main_image_path = self._copy_file_add_str(main_image_path, '_draw')
        # 画像を読み込む
        image = cv2.imread(str(main_image_path))
        # 矩形を描画する
        # rect辞書からx, y, width, heightを取り出す
        x, y, width, height = rect['x'], rect['y'], rect['width'], rect['height']
        # 矩形の色 (B, G, R) と太さを指定
        color = (0, 255, 0)  # 緑色
        thickness = 2  # 太さ
        # 矩形を描画
        cv2.rectangle(image, (x, y), (x + width, y + height), color, thickness)
        # 変更を保存するか、表示するか選べます
        # 画像を表示
        # cv2.imshow('Image with Rectangle', image)
        # cv2.waitKey(0)  # キー入力を待つ
        # cv2.destroyAllWindows()
        # または画像をファイルに保存
        cv2.imwrite(str(main_image_path), image)

    def _copy_file_add_str(self, src_path, add_str):
        """
        src_pathのファイル”名”の最後にadd_strを付与して、ファイルをコピーする
         Returns: dist_path
        """
        dist_path = _add_file_name(src_path, add_str)
        shutil.copy(src_path, str(dist_path))
        return dist_path
    
    def click_by_image(self, templete_image_path, log_image:bool=True):
        #####
        # 画像検索をして、clickする
        image_path = self.save_page_source_and_screenshot(do_page_source=False)
        self.selenium_log.add_log('main_image_path = {}'.format(image_path))
        # C:\Users\OK\source\repos\Repository4_python\scraping_test\selenium_utility\selenium_test.py
        # image_dir = Path(__file__).parent.joinpath('image/__img_selenium_test')
        # temp_img_file_name = 'youtube_logo_small.jpg'
        # templete_image_path = image_dir.joinpath(temp_img_file_name)
        # rect={'height': 5, 'width': 840, 'x': 36, 'y': 514}
        rect = self.find_image(
            image_path, templete_image_path)
        if self.rect_is_zero(rect):
            return False
        else:
            if log_image:
                self.draw_rect(image_path, rect)
            x,y = self.get_rect_center(rect)
            self.click_point(x,y)
            return True
    

    ##########
    def set_logger(self,any_logger):
        self.selenium_log = get_selenium_logger(any_logger)

    def set_driver(self,webdriver_path:str):
        self.driver:webdriver.Chrome=None
        self.page_source_ex  = None
        if not os.path.exists:
            raise Exception('path not exists. [path={}]'.format(webdriver_path))
        self.driver = webdriver.Chrome(webdriver_path,options=self.options)
        self.page_source_ex = PageSourceUtility(self.driver)

    def set_url(self, url:str):
        raise NotImplementedError()

    def get_webelement_attribute(self,element:WebElement,attr_name:str):
        if element==None:
            return 'None'
        return WebElementUtility(element).get_attribute(attr_name)

    def close(self):
        """ driver.close -> driver.quit"""
        try:
            self.driver.close()
            self.driver.quit()
        except urllib3.exceptions.MaxRetryError:
            self.selenium_log.add_log(str(e))
            # Youtube以外のURLの時ｓ
            #     raise MaxRetryError(_pool, url, error or ResponseError(cause))
            #urllib3.exceptions.MaxRetryError: HTTPConnectionPool(host='localhost', port=50573): Max retries exceeded with url: /session/45fe966c4a2647f04de5e042b125430a/window (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x0000019FBC0B79D0>: Failed to establish a new connection: [WinError 10061] 対象のコンピューターによって拒否されたため、接続できませんでした。'))
        except Exception as e:
            raise e
    
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
        
    def save_page_source_and_screenshot_with_log(
            self,add_str:str='',
            dir_path:str='',
            log_level:int=199,
            do_screenshot:bool=True,
            do_page_source:bool=True):
        """
        スクリーンショットとpage_sourceを出力する

        Returns:
            image_path
        """
        add_str = _repair_to_file_name(add_str)
        print()
        print()
        print('*****')
        image_path = ''
        source_path = ''
        if log_level < 199:
            if do_screenshot:
                ext='_chrome_image.png'
                image_path = self.get_save_path(base_name='', add_str=add_str, ext=ext, dir_path=dir_path)
                self.screenshot(image_path)
            if do_page_source:
                ext='_chrome_source.html.txt'
                source_path = self.get_save_path(base_name='', add_str=add_str, ext=ext, dir_path=dir_path)
                self.write_page_source(source_path)
            self.selenium_log.add_log('save_page_source_and_screenshot',log_level=log_level)
            self.selenium_log.add_log('source = {}'.format(source_path),log_level=log_level)
            # self.selenium_log.add_log_screenshot(image_path,'save_page_source_and_screenshot',log_level=log_level)
        else:
            print('save_page_source_and_screenshot')
            print('source = {}'.format(source_path))
            print('image = {}'.format(image_path))
        print()
        return image_path
    
    def save_page_source_and_screenshot(
            self,add_str:str='',
            dir_path:str='',
            do_screenshot:bool=True,
            do_page_source:bool=True):
        """
        スクリーンショットとpage_sourceを出力する

        Returns:
            image_path
        """
        return self.save_page_source_and_screenshot_with_log(
            add_str,dir_path,
            self.selenium_log.log_level,
            do_screenshot=do_screenshot,
            do_page_source=do_page_source)
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
            file_name = datetime.datetime.now().strftime('%Y%m%d_%H%M%S_%f') + add_str + ext
        else:
            file_name = base_name + add_str + ext
        return file_name

    def get_save_path(self,base_name:str='', add_str:str='', ext:str='', dir_path:str=''):
        """
        空ならlog_dirにyymmdd_hhmmss_chrome_source.htmlとして保存する
         log_dirが設定されているが、ない場合、
            ファイルであれば削除してdirを作成
             dirがなければ作成
              base_name=='' の時日付を付与する => YYMMDD_HHMMSS_add_str.ext

        """
        if dir_path=='':
            # dir_path = self.selenium_log.log_dir
            dir_path = self.selenium_log.get_image_dir_path()
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
            file_path = self.get_save_path('','_chrome_source.html')
        data = driver.page_source
        if len(Path(file_path).name)>200:
            file_path = Path(file_path).parent.joinpath(Path(file_path).name[:50])
        with open(file_path,'w',encoding='utf-8')as f:
            f.write(data)

    def screenshot(self,image_file_path:str=''):
        """
        chrome画面のスクリーンショットを保存する
         戻り値はスクリーンショットのファイルパス
        """
        driver = self.driver
        if image_file_path=='':
            image_file_path = self.get_save_path('','_chrome','.png')
        print('screenshot = {}'.format(image_file_path))
        # get width and height of the page
        # w = driver.execute_script("return document.body.scrollWidth;")
        # h = driver.execute_script("return document.body.scrollHeight;") # Windowがリサイズされる
        # 231123 
        # AttributeError: 'WebDriver' object has no attribute 'find_element_by_tag_name'
        # html_el = driver.find_element_by_tag_name('body') 
        # kw_search = browser.find_element(By.CSS_SELECTOR, "#sbtc > div > div.a4bIc > input")# example
        html_el = driver.find_element(By.CSS_SELECTOR, "body")
        w = html_el.size['width']
        h = html_el.size['height']
        print('screenshot w,h ={},{}'.format(w,h))
        # set window size
        # driver.set_window_size(w,h)
        # Get Screen Shot
        driver.save_screenshot(image_file_path)
        return image_file_path

    
    def get_element():
        pass


def _repair_to_file_name(value:str, max_len:int=200):
    arg_value = value
    pos = value.find('Exception:')
    if 0<=pos:
        value = value[:pos + len('Exception:')]
    else:
        value = sanitize_filename(value)
        return value
    if max_len<len(pos):
        value = value[:max_len]
    value = sanitize_filename(value)
    return value

# def _replace_char_list(char_list:'list[str]', value:str)

def sanitize_filename(filename:str):
    # Define characters that are not allowed in Windows filenames
    invalid_chars = '<>:;%"/\\|?*.,!'
    # Replace each invalid character with an underscore
    for char in invalid_chars:
        filename = filename.replace(char, '_')
    filename = filename.replace('\n','_')
    filename = filename.replace('\t','_')
    return filename


def _add_file_name(file_path, add_str):
    """
    file_path_dir / file_name + add_str + '.ext'
    """
    name = Path(file_path).stem + add_str + Path(file_path).suffix
    ret = Path(file_path).parent.joinpath(name)
    return ret   