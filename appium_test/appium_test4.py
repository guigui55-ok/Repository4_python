import datetime
import pathlib
import subprocess
import time
import os
import datetime

from subprocess import PIPE
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
import adb_desired_caps
from dummy_logger import DummyLogger

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ConstAppiumTest():
    DEFAULT_PACAGE = 'com.sega.stella'
    DEFAULT_ACTIVITY = 'com.facebook.CustomTabActivity'

class AppiumTest:
    """
    Summary:
        Appiumでモバイルアプリテストを実行するためのクラス

    Description:
        AppiumTestクラスは、モバイルアプリのテストを実行するための機能を提供します。
        アプリの起動、デバイスの制御、ページソースの保存などができます。
        また、init_objectsメソッドでロガーの初期化、set_desired_capsメソッドでテスト対象アプリの設定を行えます。
    """
    def __init__(self):
        self.address = '127.0.0.1'
        self.port = '4723'
        self.base_path = '/wd/hub'
        se0lf.timestamp = datetime.datetime.now().strftime('%y%m%d_%H%M%S')
        self.server_log_dir = pathlib.Path(__file__).parent.joinpath('log')
        self.appium_log_path = self._create_log_file_path()
        self.desired_caps = None
        self.driver=None

    def init_objects(self, log_dir:str, desired_caps=None):
        path = log_dir
        self.logger = DummyLogger(path)
        self.set_desired_caps(desired_caps)

    def _create_log_file_path(self):
        file_name = self.timestamp + '_appium_svr.log'
        return str(self.server_log_dir.joinpath(file_name))

    def start_appium_server(self):
        cmd = f'appium --log-timestamp -g {self.appium_log_path}'
        return subprocess.Popen(cmd, shell=True)
    
    def set_desired_caps(self, desired_caps=None):
        if desired_caps!=None:
            self.desired_caps = adb_desired_caps.create_desired_caps_for_android(
                ConstAppiumTest.DEFAULT_PACAGE, ConstAppiumTest.DEFAULT_ACTIVITY)


    def connect_device(self):
        url = f'http://{self.address}:{self.port}{self.base_path}'
        self.driver = webdriver.Remote(
            command_executor=url, desired_capabilities=self.desired_caps)
        return self.driver

    def control_device(self, driver: WebDriver=None):
        """
        ここに操作したいデバイスの処理を実装する
        """
        self.appium_controller = AppiumController(self)
        self.appium_controller.excute_main()

    def save_page_source(self, file_name:str='', dir:str=''):
        if dir == '':
            dir = self.server_log_dir
        if file_name == '':
            now = datetime.datetime.now()
            date_string = now.strftime('%y%m%d_%H%M%S')
            file_name = 'page_source_' + date_string + '.txt'
        _save_page_source(self.driver, file_name, dir)



class AppiumController():
    def __init__(self, appium_tester:AppiumTest) -> None:
        self.appium_tester = appium_tester

    # 以下は、AppiumTest クラス内の control_device メソッドの変更部分です。
    def excute_main(self):
        """
        ここに操作したいデバイスの処理を実装する
        """
        appium_tester = self.appium_tester
        driver = appium_tester.driver
        dir = str(pathlib.Path(__file__).parent)
        _save_page_source(driver, 'page_source.txt', __file__)
        # value = "//android.widget.Button[@text='Yes']"
        value = "//*[@text='設定']"
        el = driver.find_element(By.XPATH, value)
        el.click()
        # driver.press_keycode(3)  # KEYCODE_HOME (ホームボタン)
        time.sleep(2)

        # # 「Chrome」アイコンを探してタップする
        # chrome_icon_xpath = "//android.widget.TextView[@content-desc='Chrome']"
        # try:
        #     WebDriverWait(driver, 10).until(
        #         EC.presence_of_element_located((By.XPATH, chrome_icon_xpath))
        #     )
        #     chrome_icon = driver.find_element_by_xpath(chrome_icon_xpath)
        #     chrome_icon.click()
        # except Exception as e:
        #     print(f"Error: {e}")

def _save_page_source(driver:WebDriver, file_name:str, dir:str):
    if os.path.isfile(dir):
        dir = os.path.dirname(dir)
    path = str(pathlib.Path(dir).joinpath(file_name))
    page_source =driver.page_source
    with open(path, 'w', encoding='utf-8')as f:
        f.write(page_source)



def _test_main():
    appium_test = AppiumTest()
    appium_test.server_log_dir = pathlib.Path(r'C:\Users\OK\source\repos\test_media_files\appium_log')
    appium_test.init_objects(appium_test.server_log_dir)
    appium_test.appium_log_path = appium_test._create_log_file_path()
    appium_process = appium_test.start_appium_server()
    time.sleep(5)

    try:
        driver = appium_test.connect_device()
        time.sleep(3)
        appium_test.control_device(driver)
        driver.quit()
    except Exception as e:
        print(f"Error: {e}")
    finally:
        appium_process.kill()
        outs, errs = appium_process.communicate()

        if outs:
            print(f"outs = {outs.decode('utf-8', 'ignore')}")
        if errs:
            new_line = '\n'
            print(f"errs = {errs.decode('utf-8').split(new_line)}")

if __name__ == '__main__':
    _test_main()