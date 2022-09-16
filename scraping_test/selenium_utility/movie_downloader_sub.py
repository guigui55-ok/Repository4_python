
if __name__ == '__main__':
    import pathlib,sys
    path = str(pathlib.Path(__file__).parent.parent)
    sys.path.append(path)

# from selenium_utility.selenium_webdriver.webdriver_utility import WebDriverUtility,WebElementUtility
# if __name__ == '__main__':
#     from movie_downloader import MovieDownloader
# else:
#     from selenium_utility.movie_downloader import MovieDownloader
from selenium_utility.selenium_webdriver.selenium_log import SeleniumLogger
from selenium_webdriver.general import Waiter
import selenium_webdriver.selenium_const
from selenium_webdriver.selenium_const import ConstResult,BAR

import time
from selenium.webdriver.remote.webdriver import WebElement
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium_webdriver.webdriver_utility import WebDriverUtility,WebElementUtility

from html_log.html_logger import HtmlLogger,BasicLogger


def get_vd_site_url():
    path = r'C:\Users\OK\source\repos\Test\movie_data\vd_main_url.txt'
    with open(path,'r',encoding='utf-8')as f:
        buf = f.read()
    return buf
def get_vd_site_url2():
    path = r'C:\Users\OK\source\repos\Test\movie_data\vd_main_url2.txt'
    with open(path,'r',encoding='utf-8')as f:
        buf = f.read()
    return buf

class DonwloadSite():
    def __init__(self,chrome_driver_path:str,html_logger:HtmlLogger) -> None:
        self.downloader_url = 'https://www.y2mate.com/jp/youtube/' #YouTubeDownloader
        self.downloader_url = ''
        if chrome_driver_path == '' or chrome_driver_path==None:
            self.chrome_driver_path = r'C:\Users\OK\source\programs\chromedriver_win32\chromedriver'
        else:
            self.chrome_driver_path = chrome_driver_path
        self.movie_url = ''
        self.chrome:WebDriverUtility=None
        self.log_dir_path = ''
        self.is_need_observer = True
        self.download_result = False
        self.logger = html_logger
    def set_log_path(self,dir_path:str):
        # self.chrome.selenium_log.set_log_dir(dir_path)
        self.log_dir_path = dir_path
    def add_log(self,value:str):
        self.logger.add_log(value)
    def open_web_site(self):
        is_downloded:bool = False
        chrome_driver_path = self.chrome_driver_path
        if self.chrome == None:
            self.chrome = WebDriverUtility(chrome_driver_path , self.logger)
        self.chrome.selenium_log.log_dir = self.logger.logger_dir_path
        self.chrome.driver.set_window_size(800,800)
        downloader_url=self.downloader_url
        self.chrome.driver.get(downloader_url)
        self.chrome.timer.wait()
        self.chrome.save_page_source_and_screenshot('_open_web')
        return True
    def change_url(self,url):
        self.chrome.driver.get(url)
        self.chrome.timer.wait()
        self.chrome.save_page_source_and_screenshot('_change_url')
    def open_web_site_and_create_driver(self,new_url:str):
        chrome_driver_path = self.chrome_driver_path
        new_chrome = WebDriverUtility(chrome_driver_path)
        new_chrome.selenium_log.log_dir = self.logger.logger_dir_path
        new_chrome.driver.set_window_size(800,800)
        downloader_url=new_url
        new_chrome.driver.get(downloader_url)
        new_chrome.timer.wait()
        new_chrome.save_page_source_and_screenshot('_open_web_new')
        return new_chrome
    def close(self):
        self.chrome.close()
    def print_result(self,flag:int,value:str,url:str=''):
        print()
        self.add_log(BAR)
        if flag==ConstResult.OK:
            self.add_log(value + '   OK')
        if flag==ConstResult.NG:
            self.add_log(value + '   NG')
        if flag==ConstResult.ERROR:
            self.add_log(value + '   ERR')
        if flag==ConstResult.NOTHING:
            self.add_log(value + '   NOTHING')
        if url!='':
            self.add_log('url = {}'.format(url))

class YouTube(DonwloadSite):
    def __init__(self, chrome_driver_path: str = '',logger:HtmlLogger=None) -> None:
        super().__init__(chrome_driver_path, logger)
        self.downloader_url = 'https://www.y2mate.com/jp/youtube'

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
        if not flag:return
        ret_int = self.wait_shown_until_download_button()
        if not flag:return
        #ENTER後にサイズが更新される
        self.chrome.driver.set_window_size(800,800)
        if ret_int == ConstResult.ERROR or ret_int == ConstResult.NOTHING: return
        flag = self.click_download()
        return flag
    
    def url_is_valid(self,url:str):
        """URLが有効か確認する
        （youtubeのものか）
        https://www.youtube.com/watch?v=AAaAAaa00Aa
        """
        check = 'https://www.youtube.com/'
        if url.startswith(check):
            return True
        self.add_log('url is invalid. > continue  url = {}'.format(url))
        return False

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
                self.add_log('waiting select movie(after send url).')
            else:
                self.add_log('prepared select movie(after send url).')
                return True
        else:
            msg = 'ERROR__prepared select movie(after send url)'
            self.add_log('ERROR')
            self.add_log(msg)
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
            el_text = WebElementUtility(element).get_attribute('text')
            if el_text.find('ダウンロード')>=0:
                # self.chrome.save_page_source_and_screenshot('click_download')
                element.click()
                return True
            elif el_text.find(' \xa0 Download ') >= 0:
                element.click()
                return True
            else:
                # print('[{}]'.format(WebElementUtility(element).get_attribute('text')))
                pass
            element.send_keys(Keys.TAB)
        else:
            self.add_log('ダウンロードボタンがない。')
            return False
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
                self.add_log('ERROR')
                self.add_log(msg)
                self.chrome.save_page_source_and_screenshot(msg)
                #ファイルを移動するためにTrueで返す
                self.print_result(ConstResult.NOTHING,msg,self.movie_url)
                return ConstResult.NOTHING
            if not self.chrome.page_source_ex.is_exists_find_all(prepared_value):
                self.chrome.timer.wait()
                self.add_log('waiting download button.[{}]'.format(i))
            else:
                self.add_log('prepared download button.')
                return ConstResult.OK
        else:
            msg = 'ERROR__not prepared download button'
            self.add_log('ERROR')
            self.add_log(msg)
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
                self.add_log(href)
                element.click()
                self.chrome.timer.wait()
                return True
        return False

    def download_movie_bef(self,url):
        """
        ダウンロード債をを開いてURLを入力、STARTをクリックして、動画をWeb上で取得する。
        その後、画面が切り替わったらダウンロードをクリックして、
        ポップアップした要素の（前とは別の）ダウンロードをクリックする。"""
        self.add_log(url)
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



class VdSite(DonwloadSite):
    def __init__(self, chrome_driver_path: str = '',logger:HtmlLogger=None) -> None:
        super().__init__(chrome_driver_path,logger,logger)
        self.chrome_driver_path = chrome_driver_path
        self.downloader_url = self.read_url()

    def read_url(self):
        path = r'C:\Users\OK\source\repos\Test\movie_data\vd_url.txt'
        with open(path,'r',encoding='utf-8')as f:
            buf = f.read()
        return buf
    def url_is_vd_main(self,url:str):
        chk = get_vd_site_url()
        if url.startswith(chk):
            return True
        return False
    def excute_download_movie(self,movie_url):
        """
        ダウンロードを開いてURLを入力、STARTをクリックして、動画をWeb上で取得する。
        その後、画面が切り替わったらダウンロードをクリックして、
        ポップアップした要素の（前とは別の）ダウンロードをクリックする。"""
        # この場合はそのまま開く
        self.downloader_url = movie_url
        self.install_addon()
        flag = super().open_web_site()
        if not flag:return
        # wait
        new_url = self.is_shown_implemented_error_screen()
        if new_url!='':
            self.downloader_url = new_url
            # new_chrome = super().open_web_site_and_create_driver(new_url)
            # new_chrome.timer.wait()
            # new_chrome.close()
            flag = self.change_url(new_url)
            flag = self.download_movie_vd_main()
        elif self.url_is_vd_main(movie_url):
            flag = self.download_movie_vd_main()

        # self.chrome.save_page_source_and_screenshot('_test')
        self.is_need_observer = False
        self.download_result = True

        # flag = self.input_movie_url(movie_url)
        # if not flag:return
        # self.movie_url = movie_url
        # #ENTER後にサイズが更新される
        # self.chrome.driver.set_window_size(800,800)
        # flag = self.wait_shown_movie_select_screen()
        # if not flag:return
        # # self.chrome.save_page_source_and_screenshot('test')
        # flag = self.select_quality_download_movie()
        # if not flag:return
        # ret_int = self.wait_shown_until_download_button()
        # if not flag:return
        # #ENTER後にサイズが更新される
        # self.chrome.driver.set_window_size(800,800)
        # if ret_int == ConstResult.ERROR or ret_int == ConstResult.NOTHING: return
        # flag = self.click_download()
        return flag
        
    def url_is_valid(self,url:str):
        """
        URLが有効か確認する
        """
        check = get_vd_site_url()
        if url.startswith(check):
            return True
        check = get_vd_site_url2()
        if url.startswith(check):
            return True
        self.add_log('url is invalid. > continue  url = {}'.format(url))
        return False
    
    def install_addon(self,path:str='',id:str=''):
        path = r'C:\Users\OK\AppData\Local\Google\Chrome\User Data\Default\Extensions\iogidnfllpdhagebkblkgbfijkbkjdmm\1.3.8_0'
        # self.chrome = WebDriverUtility()
        self.chrome = WebDriverUtility()
        self.chrome.install_addon(path)
        self.chrome.set_driver(self.chrome_driver_path)
        # ID: iogidnfllpdhagebkblkgbfijkbkjdmm
        # Mac
        # /Users/<ユーザー名>/Library/Application\ Support/Google/Chrome/Default/Extensions/
        # Windows
        # C:\Users\<ユーザ名>\AppData\Local\Google\Chrome\User\Data\Default\Extensions
        # https://yuki.world/selenium-load-chrome-extension/



    def download_movie_vd_main(self):
        flag = self.tap_play()
        if not flag: return
        # self.chrome.open_new_tab('https://www.hlsloader.com/ja/irec.html')
        
        self.chrome.timer.wait()
        flag = self.run_chrome_extention()
        if not flag: return
        flag = self.download_stream_recorder()
        if not flag: return
        flag = self.tap_save_button()
        self.chrome.save_page_source_and_screenshot('_down_after_ext')
        return flag

    def tap_play(self):
        movie_class = 'video-bg-pic'
        el = self.chrome.driver.find_element_by_class_name(movie_class)
        x,y = WebElementUtility(el).get_center_position()
        self.add_log('tap ({} , {})'.format(x,y))
        self.chrome.click_by_position(x ,y)
        ###
        self.chrome.save_page_source_and_screenshot('_after_play1')
        self.chrome.timer.wait_long()
        self.chrome.save_page_source_and_screenshot('_after_play2')
        self.chrome.timer.wait_long()
        self.chrome.save_page_source_and_screenshot('_after_play3')
        for _ in range(3):
            cl_name = 'videoad-skip-txt'
            try:
                el = self.chrome.driver.find_element_by_class_name(cl_name)
                el.click()
                break
            except:
                pass
            self.chrome.save_page_source_and_screenshot('_after_play4')
            self.chrome.timer.wait()
        self.chrome.timer.wait_long()
        self.chrome.save_page_source_and_screenshot('_after_play5')
        return True
        ### 再生要素がjabascriptないで、TABでは選択できない
        # ## text , class  , id  , rect
        # None   embed-responsive desktop      html5video   [[0, 151], [734, 598]]
        # None   embed-responsive-item      hlsplayer   [[0, 151], [734, 598]]
        # None   video-bg-pic         [[0, 151], [734, 598]]
        #play
        # tap_value = 'mobile-only-show ad-footer ad-support-desktop'
        # play_el = self.chrome.driver.find_element_by_class_name(value)
        # play_el = self.find_by_tab_key(tap_value,'class',110)
        # label_main_value = 'btn btn-default label main uploader-tag hover-name'
        # click_title = '再生'
        ## el = self.chrome.driver.find_element_by_link_text('再生') # Unable to locate element
        # els = self.chrome.driver.find_elements_by_xpath('//*')
        # for el in els:
        #     # text = self.chrome.get_webelement_attribute(el,'text')
        #     cl_name = self.chrome.get_webelement_attribute(el,'class')
        #     # title = self.chrome.get_webelement_attribute(el,'title')
        #     # id = self.chrome.get_webelement_attribute(el,'id')
        #     # rect = WebElementUtility(el).get_rect()
        #     # if rect[0][0] >= 0:
        #     #     print(text + '   ' + cl_name + '   ' + title +  '   ' + id + '   {}'.format(rect))
        #     print('.',end='')
        #     if cl_name == movie_class:
        #         print('   finded.' + cl_name)
        #         x,y = WebElementUtility(el).get_center_position()
        #         print('tap ({} , {})'.format(x,y))
        #         self.chrome.click_by_position(x + 0 , y + 0)
        #         ## play_el.click() #ElementNotInteractableException element not interactable 要素は相互作用できません
        #         self.chrome.timer.wait()
        #         break
        #     end_val = 'previewimg'
        #     if cl_name == end_val:
        #         break
        ###

    def run_chrome_extention(self):
        def wait_this():
            # self.chrome.timer.wait_short()
            self.chrome.timer.wait(0.5)
        import pyautogui
        pyautogui.hotkey('alt','shift','t')
        wait_this()
        for _ in range(5):
            pyautogui.hotkey('left')
            wait_this()
            
        pyautogui.hotkey('enter')
        wait_this()
        for _ in range(2):
            pyautogui.hotkey('down')
            wait_this()
        
        pyautogui.hotkey('enter')
        wait_this()

        self.chrome.change_tab(1)
        return True
    
    def is_shown_save_button_in_download_page(self):
        # Message: no such element: Unable to locate element: {"method":"link text","selector":"保存"}
        # 'Message: no such element: Unable to locate element: {"method":"link text","selector":"停止"}\n  (Session info: chrome=102.0.5005.63)\n'
        try:
            # el = self.chrome.driver.find_element_by_link_text('保存')
            # value = 'saveButton btn btn-primary'
            # el = self.chrome.driver.find_element_by_class_name(value)
            # value = '停止'
            # el = self.chrome.driver.find_element_by_link_text('停止')
            # none_val = 'display:none'
            # style = WebElementUtility(el).get_attribute('style')
            # if style == none_val:
                # return False
            

            value = 'progress'
            cl_el= self.chrome.driver.find_element_by_class_name(value)
            cl_val = WebElementUtility(cl_el).get_attribute('style')
            val = WebElementUtility(cl_el).get_attribute('value')
            max = WebElementUtility(cl_el).get_attribute('max')
            if int(val) > 0:
                self.download_progress_value = int(val)
            else:
                if self.download_progress_value > 0 and int(val)==0:
                    return True
            self.add_log(' {}  /  {}'.format(val,max))
            if val == max:
                return True
            ###
            value = '<title>完了'
            is_complete = self.chrome.page_source_ex.is_exists_find_all(value,True)
            return is_complete

            # if cl_val.startswith('width: 100%'):
            #     return True
            # return False
            # value = 'progressLabel'
            # cl_el= self.chrome.driver.find_element_by_class_name(value)
            # # cl_el = cl_parent_el.find_element(value)
            # cl_val = cl_el.get_attribute('text')
            # cl_val = WebElementUtility(cl_el).get_attribute('text')
            # cl_val = self.chrome.get_webelement_attribute()
            # sepalete = ' / '
            # pos = cl_val.find(sepalete)
            # bef = cl_val[:pos-1]
            # aft = cl_val[pos+len(sepalete)+1:]
            # if bef == aft:
            #     return True
            # return False

            value = 'style="display:none">保存</button>'
            is_exists = self.chrome.page_source_ex.is_exists_find_all(value,True)
            return not is_exists
        except Exception as e:
            str_e = str(e)
            return False
    
    
    def is_shown_save_button_in_download_page_(self):
        # Message: no such element: Unable to locate element: {"method":"link text","selector":"保存"}
        try:
            el = self.chrome.driver.find_element_by_link_text('保存')
            none_val = 'display:none'
            style = WebElementUtility(el).get_attribute('style')
            if style == none_val:
                return False
            return True
        except:
            return False
    
    def download_stream_recorder(self):
        el = self.chrome.driver.find_element_by_link_text('ストレコ')
        if el == None:
            self.add_log('ストレコが起動していない。')
            return False
        el = self.chrome.driver.find_element_by_class_name('titleLabel')
        title = WebElementUtility(el).get_attribute('text')
        self.add_log('title [{}]'.format(title))
        time_log_flag = False
        count = 0
        check_limit_min = 10            
        start = time.time()
        self.download_progress_value = -1
        while not self.is_shown_save_button_in_download_page():
            passed_time = time.time() - start
            if passed_time > (check_limit_min*60):
                print()
                self.add_log('time passed to limit. passed_time = {}'.format(passed_time))
                break
            if not time_log_flag:
                if int(passed_time) % 5==0:
                    self.add_log('downloading...[{} sec]'.format(count*5))
                    count +=1
                    time_log_flag = True
            else:
                if int(passed_time) % 6==0:
                    time_log_flag = False

            time.sleep(2)
            try:
                # 例外
                pass
            except:
                # self.add_log('file size check error.  path = {}'.format(target))
                is_passed_loop = True
        return True

    def tap_save_button(self):
        # value = '保存'
        # el = self.find_by_tab_key(value,'text')
        value = 'saveButton btn btn-primary'
        el = self.find_by_tab_key(value,'class')
        if el!=None:
            el.click()
            return True
        return False


    
    def find_by_tab_key(self,find_value:str,attr_name:str,tab_retry:int=30):
        """
        タブキーで値を探しながら、要素を探す
          エラー対策
         selenium.common.exceptions.NoSuchElementException: Message: no such element: Unable to locate element: {"method":"css selector","selector":".mobile-hide ad-square ad-support-desktop"}
  (Session info: chrome=102.0.5005.63)
        """
        element:WebElement=None
        count = tab_retry
        for _ in range(count):
            self.chrome.timer.wait_little()
            element = self.chrome.driver.switch_to.active_element
            el_text = WebElementUtility(element).get_attribute(attr_name)
            if el_text.find(find_value)>=0:
                # self.chrome.save_page_source_and_screenshot('click_download')
                # element.click()
                return element
            else:
                WebElementUtility(element).print_attributes_for_analyze()
                # print('[{}]'.format(WebElementUtility(element).get_attribute(attr_name)))
                pass
            element.send_keys(Keys.TAB)
        else:
            self.add_log('[{}({})]がない。'.format(find_value,attr_name))
            return None
    
    def is_shown_implemented_error_screen(self):
        value = '<strong>予期せぬエラーが発生しました'
        if self.chrome.page_source_ex.is_exists_find_all(value,True):
            el = self.chrome.driver.find_element_by_class_name('_on-error')
            a_tag = el.find_element_by_tag_name('a')
            url = self.chrome.get_webelement_attribute(a_tag,'href')
            return url
        return ''

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
                self.add_log('waiting select movie(after send url).')
            else:
                self.add_log('prepared select movie(after send url).')
                return True
        else:
            msg = 'ERROR__prepared select movie(after send url)'
            self.add_log('ERROR')
            self.add_log(msg)
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
            el_text = WebElementUtility(element).get_attribute('text')
            if el_text.find('ダウンロード')>=0:
                # self.chrome.save_page_source_and_screenshot('click_download')
                element.click()
                return True
            elif el_text.find(' \xa0 Download ') >= 0:
                element.click()
                return True
            else:
                # print('[{}]'.format(WebElementUtility(element).get_attribute('text')))
                pass
            element.send_keys(Keys.TAB)
        else:
            self.add_log('ダウンロードボタンがない。')
            return False
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
                self.add_log('ERROR')
                self.add_log(msg)
                self.chrome.save_page_source_and_screenshot(msg)
                #ファイルを移動するためにTrueで返す
                self.print_result(ConstResult.NOTHING,msg,self.movie_url)
                return ConstResult.NOTHING
            if not self.chrome.page_source_ex.is_exists_find_all(prepared_value):
                self.chrome.timer.wait()
                self.add_log('waiting download button.[{}]'.format(i))
            else:
                self.add_log('prepared download button.')
                return ConstResult.OK
        else:
            msg = 'ERROR__not prepared download button'
            self.add_log('ERROR')
            self.add_log(msg)
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
                self.add_log(href)
                element.click()
                self.chrome.timer.wait()
                return True
        return False



def main():
    dir_path = r'C:\ZMyFolder\newDoc\新しいfiles\_test_movie'
    import os
    file_name = r'test.url'
    # file_name = r'.url'
    path = os.path.join(dir_path,file_name)
    import pathlib
    # log_dir_path = str(pathlib.Path(__file__).parent.joinpath('log')) 
    selenium_log_dir = r'C:\Users\OK\source\repos\test_media_files\selenium_log'
    log_dir_path = selenium_log_dir
    logger = BasicLogger(log_dir_path)
    from movie_downloader import MovieDownloader
    url = MovieDownloader().get_url_from_link(path)
    print(url)

    from download_directoy_observer import DownloadDirectoryObserver,DEFAULT_DONLOAD_DIR
    observer = DownloadDirectoryObserver(DEFAULT_DONLOAD_DIR,logger)
    observer
    is_downloded:bool = False
    chrome_driver_path = r'C:\Users\OK\source\programs\chromedriver_win32\chromedriver'
    if url.startswith('https://www.youtube.com/'):
        downloader:YouTube = YouTube(chrome_driver_path,logger)
    elif url.startswith(get_vd_site_url()):
        downloader:VdSite = VdSite(chrome_driver_path,logger) #VdMainSite
    elif url.startswith(get_vd_site_url2()):
        downloader:VdSite = VdSite(chrome_driver_path,logger)
    else:
        msg = 'YouTube以外は未実装'
        raise Exception(msg)
        downloader:DonwloadSite(chrome_driver_path)
    # downloader.set_log_path(selenium_log_dir)
    
    if isinstance(downloader,YouTube) \
    or isinstance(downloader,VdSite) \
    or isinstance(downloader,DonwloadSite):
        # downloader.set_log_path(log_dir_path)
        is_downloded = downloader.excute_download_movie(url)
    flag = observer.excute()
    downloader.close()
    if flag:
        print('DOWNLOAD SUCCESS.')
    else:
        print('DOWLNLOAD FAILED.')
    return is_downloded

if __name__ == '__main__':
    main()