


# from selenium_utility.selenium_webdriver.webdriver_utility import WebDriverUtility,WebElementUtility
from selenium_webdriver.general import Waiter
import selenium_webdriver.selenium_const
from selenium_webdriver.selenium_const import ConstResult,BAR

import time
from selenium.webdriver.remote.webdriver import WebElement
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium_webdriver.webdriver_utility import WebDriverUtility,WebElementUtility


class DonwloadSite():
    def print_result(self,flag:int,value:str,url:str=''):
        print()
        print(BAR)
        if flag==ConstResult.OK:
            print(value + '   OK')
        if flag==ConstResult.NG:
            print(value + '   NG')
        if flag==ConstResult.ERROR:
            print(value + '   ERR')
        if flag==ConstResult.NOTHING:
            print(value + '   NOTHING')
        if url!='':
            print('url = {}'.format(url))
            
    def __init__(self,chrome_driver_path:str='') -> None:
        self.downloader_url = 'https://www.y2mate.com/jp/youtube/aBRbm6a9vs4' #YouTubeDownloader
        self.downloader_url = ''
        if chrome_driver_path == '':
            self.chrome_driver_path = r'C:\Users\OK\source\programs\chromedriver_win32\chromedriver'
        else:
            self.chrome_driver_path = chrome_driver_path
        self.movie_url = ''
        self.chrome:WebDriverUtility=None
        self.log_dir_path = ''
    def set_log_path(self,dir_path:str):
        # self.chrome.selenium_log.set_log_dir(dir_path)
        self.log_dir_path = dir_path
    def open_web_site(self):
        is_downloded:bool = False
        chrome_driver_path = self.chrome_driver_path
        self.chrome = WebDriverUtility(chrome_driver_path)
        self.chrome.selenium_log.log_dir = self.log_dir_path
        self.chrome.driver.set_window_size(800,800)
        downloader_url=self.downloader_url
        self.chrome.driver.get(downloader_url)
        self.chrome.timer.wait()
        return True
    def close(self):
        self.chrome.close()


class YouTube(DonwloadSite):
    def __init__(self, chrome_driver_path: str = '') -> None:
        super().__init__(chrome_driver_path)
        self.downloader_url = 'https://www.y2mate.com/jp/youtube/aBRbm6a9vs4'

    def excute_download_movie(self,movie_url):
        """
        ダウンロードを開いてURLを入力、STARTをクリックして、動画をWeb上で取得する。
        その後、画面が切り替わったらダウンロードをクリックして、
        ポップアップした要素の（前とは別の）ダウンロードをクリックする。"""
        flag = super().open_web_site()
        if not flag:return
        flag = self.input_movie_url(movie_url)
        if not flag:return
        self.movie_url = movie_url
        #ENTER後にサイズが更新される
        self.chrome.driver.set_window_size(800,800)
        flag = self.wait_shown_movie_select_screen()
        if not flag:return
        # self.chrome.save_page_source_and_screenshot('test')
        flag = self.select_quality_download_movie()
        ret_int = self.wait_shown_until_download_button()
        #ENTER後にサイズが更新される
        self.chrome.driver.set_window_size(800,800)
        if ret_int == ConstResult.ERROR or ret_int == ConstResult.NOTHING: return
        flag = self.click_download()
        return flag
    

    def input_movie_url(self,movie_url):
        chrome = self.chrome
        input_el = chrome.driver.find_element_by_tag_name('input')
        input_el.click()
        chrome.timer.wait_short()
        for _ in range(int(2)):
            input_el.send_keys(Keys.DELETE)
            chrome.timer.wait_short()
            if WebElementUtility(input_el).util.get_value()=='':
                break
        chrome.timer.wait()
        input_el.send_keys(movie_url)
        chrome.timer.wait()
        input_el.send_keys(Keys.ENTER)
        chrome.timer.wait()
        chrome.timer.wait()
        return True
    
    def wait_shown_movie_select_screen(self):
        """
        StartをENTER後に、動画が取得されていなければ、一番下まで行くことがある（TABを押しているので）
         動画を取得（画面が更新される）まで待つ
          <div id="result"></div>がなければ、動画を取得している
        """
        prepared_value_after_enter = '<div id="result"></div>'
        limit = 20
        for _ in range(limit):
            if self.chrome.page_source_ex.is_exists_find_all(prepared_value_after_enter):
                self.chrome.timer.wait()
                print('waiting select movie(after send url).')
            else:
                print('prepared select movie(after send url).')
                return True
        else:
            msg = 'ERROR__prepared select movie(after send url)'
            print('ERROR')
            print(msg)
            self.chrome.save_page_source_and_screenshot(msg)
            self.print_result(ConstResult.ERROR,msg,self.movie_url)
            return False
        return False
    
    def select_quality_download_movie(self):
        """
        画質を選択する
        """
        element:WebElement=None
        count = 20
        for _ in range(count):
            self.chrome.timer.wait_little()
            element = self.chrome.driver.switch_to.active_element
            if WebElementUtility(element).get_attribute('text').find('ダウンロード')>=0:
                # self.chrome.save_page_source_and_screenshot('click_download')
                element.click()
                return True
            element.send_keys(Keys.TAB)
        self.chrome.timer.wait(0.2)
        # chrome.save_page_source_and_screenshot('waiting_save_button')
        return False
    
    def wait_shown_until_download_button(self):
        """
        ダウンロードボタンが出るまで待つ（ポップアップで出る）
        """
        # wait_value = 'Please wait while the file is being prepared for downloading'
        prepared_value = 'form-group has-success has-feedback'
        limit = 60
        for i in range(limit):
            if self.chrome.page_source_ex.is_exists_find_all('<span class="sr-only">Error:',False):
                msg = 'ERROR__shown error screen NOTHING'
                print('ERROR')
                print(msg)
                self.chrome.save_page_source_and_screenshot(msg)
                #ファイルを移動するためにTrueで返す
                self.print_result(ConstResult.NOTHING,msg,self.movie_url)
                return ConstResult.NOTHING
            if not self.chrome.page_source_ex.is_exists_find_all(prepared_value):
                self.chrome.timer.wait()
                print('waiting download button.[{}]'.format(i))
            else:
                print('prepared download button.')
                return ConstResult.OK
        else:
            msg = 'ERROR__not prepared download button'
            print('ERROR')
            print(msg)
            self.chrome.save_page_source_and_screenshot(msg)
            self.print_result(ConstResult.ERROR,msg,self.movie_url)
            return ConstResult.ERROR

    def click_download(self):
        """
        ダウンロードボタンをクリックする
        """
        elements = self.chrome.driver.find_elements_by_tag_name('a')
        for element in elements:
            cls = WebElementUtility(element).get_attribute('class')
            if cls == 'btn btn-success btn-file':
                href = WebElementUtility(element).get_attribute('href')
                print(href)
                element.click()
                self.chrome.timer.wait()
                return True
        return False

    def download_movie_bef(self,url):
        """
        ダウンロード債をを開いてURLを入力、STARTをクリックして、動画をWeb上で取得する。
        その後、画面が切り替わったらダウンロードをクリックして、
        ポップアップした要素の（前とは別の）ダウンロードをクリックする。"""
        print(url)
        # import time
        # from selenium.webdriver.remote.webdriver import WebElement
        # from selenium.webdriver.common.keys import Keys
        # from selenium.webdriver.common.by import By
        # from selenium_webdriver.webdriver_utility import WebDriverUtility
        # from selenium_webdriver.webdriver_utility import WebElementUtility
        # # from selenium_webdriver.webdriver_utility import WebElement
        # # from selenium_webdriver.webdriver_utility import By
        # # from selenium_webdriver.webdriver_utility import keys
        # is_downloded:bool = False
        # chrome_driver_path = self.chrome_driver_path
        # chrome = WebDriverUtility(chrome_driver_path)
        # try:
        #     chrome.driver.set_window_size(800,800)
        #     downloader_url=self.downloader_url
        #     chrome.driver.get(downloader_url)
        #     chrome.timer.wait()

        #     input_el = chrome.driver.find_element_by_tag_name('input')
        #     input_el.click()
        #     chrome.timer.wait_short()
        #     for _ in range(int(3)):
        #         input_el.send_keys(Keys.DELETE)
        #         chrome.timer.wait_short()
        #         if WebElementUtility(input_el).util.get_value()=='':
        #             break
        #     chrome.timer.wait()
        #     input_el.send_keys(url)
        #     chrome.timer.wait()
        #     # self.wait_long()
        #     # value = 'Start'
        #     # # button_el = chrome.driver.find_element_by_tag_name('button')
        #     # buttons = chrome.driver.find_elements_by_tag_name('button')
        #     # button:WebElement=None
        #     # for button in buttons:
        #     #     if chrome.get_webelement_attribute(button,'value') == 'Start':
        #     #         button.click()
        #     #         break
        #     input_el.send_keys(Keys.ENTER)
        #     chrome.timer.wait()
        #     chrome.timer.wait()

        #     #ENTER後にサイズが更新される
        #     chrome.driver.set_window_size(800,800)

        #     # chrome.save_page_source_and_screenshot('after_enter2')


        #     # StartをENTER後に、動画が取得されていなければ、一番下まで行くことがある（TABを押しているので）
        #     # 動画を取得（画面が更新される）まで待つ
        #     # <div id="result"></div>がなければ、動画を取得している
        #     prepared_value_after_enter = '<div id="result"></div>'
        #     limit = 20
        #     for _ in range(limit):
        #         if chrome.page_source_ex.is_exists_find_all(prepared_value_after_enter):
        #             chrome.timer.wait()
        #             print('waiting select movie(after send url).')
        #         else:
        #             print('prepared select movie(after send url).')
        #             break
        #     else:
        #         msg = 'ERROR__prepared select movie(after send url)'
        #         print('ERROR')
        #         print(msg)
        #         chrome.save_page_source_and_screenshot(msg)
        #         self.print_result(ConstResult.ERROR,msg,url)
        #         return False

        #     element:WebElement=None
        #     count = 20
        #     for _ in range(count):
        #         chrome.timer.wait_little()
        #         element = chrome.driver.switch_to.active_element
        #         if WebElementUtility(element).get_attribute('text').find('ダウンロード')>=0:
        #             chrome.save_page_source_and_screenshot('click_download')
        #             element.click()
        #             break
        #         element.send_keys(Keys.TAB)
        #     chrome.timer.wait(0.2)
        #     # chrome.save_page_source_and_screenshot('waiting_save_button')

        #     # wait_value = 'Please wait while the file is being prepared for downloading'
        #     prepared_value = 'form-group has-success has-feedback'
        #     limit = 60
        #     for i in range(limit):
        #         if chrome.page_source_ex.is_exists_find_all('<span class="sr-only">Error:',False):
        #             msg = 'ERROR__shown error screen NOTHING'
        #             print('ERROR')
        #             print(msg)
        #             chrome.save_page_source_and_screenshot(msg)
        #             #ファイルを移動するためにTrueで返す
        #             self.print_result(ConstResult.NOTHING,msg,url)
        #             return True
        #         if not chrome.page_source_ex.is_exists_find_all(prepared_value):
        #             chrome.timer.wait()
        #             print('waiting download button.[{}]'.format(i))
        #         else:
        #             print('prepared download button.')
        #             break
        #     else:
        #         msg = 'ERROR__not prepared download button'
        #         print('ERROR')
        #         print(msg)
        #         chrome.save_page_source_and_screenshot(msg)
        #         self.print_result(ConstResult.ERROR,msg,url)
        #         return False


        #     # self.wait(10)
        #     # import pathlib
        #     # path = str(pathlib.Path(__file__).parent.joinpath('page_source.txt'))
        #     # chrome.write_page_source(path)

        #     elements = chrome.driver.find_elements_by_tag_name('a')
        #     for element in elements:
        #         cls = WebElementUtility(element).get_attribute('class')
        #         if cls == 'btn btn-success btn-file':
        #             href = WebElementUtility(element).get_attribute('href')
        #             print(href)
        #             element.click()
        #     # value = 'form-group has-success has-feedback'
        #     # element = chrome.driver.find_element_by_class_name(value)
        #     #Message: no such element: Unable to locate element: {"method":"css selector","selector":".form-group has-success has-feedback"}
        #     #(Session info: chrome=102.0.5005.63)
        #     return is_downloded
        #     # if not is_downloded:
        #     #     return is_downloded
        #     # is_downloded = True

        #     # while(True):
        #     #     if text_is_false():
        #     #         break
        #     #     self.wait(20)
        # except Exception as e:
        #     # print(str(e))
        #     import traceback
        #     print()
        #     print(BAR)
        #     traceback.print_exc()
        #     self.print_result(ConstResult.ERROR,str(e))
        #     is_downloded = False
        #     return is_downloded
        # finally:
        #     chrome.close()
        #     return is_downloded
