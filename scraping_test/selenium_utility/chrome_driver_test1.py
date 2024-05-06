
from pathlib import Path

import time
class Timer():
    def __init__(self) -> None:
        self.default_time = 1
    
    def _get_time(self, wait_time=None):
        if wait_time == None:
            return self.default_time
        else:
            return float(self.default_time)

    def wait(self, wait_time=None):
        wait_time = self._get_time(wait_time)
        print('Wait Start {} sec.'.format(wait_time), end='', flush=True)
        time.sleep(wait_time)
        print('  End.', flush=True)
    
    def wait_short(self, wait_time=None):
        wait_time = self._get_time(wait_time)
        wait_time = wait_time/2
        self.wait(wait_time)


class SimpleLogger():
    def __init__(self) -> None:
        self.path = ''
    
    def init_parameter(self, logger_path):
        self.path = Path(logger_path)
        self.dir = self.path.parent
        self.text_path = self.path
    
    def put_log(self, text:str):
        _put_log(self.path, text)
    
    def take_screenshot(self, text:str):
        pass

class DriverLogger(SimpleLogger):
    pass

import datetime
ENCODING = 'utf-8'
NEW_LINE = '\n'
def _put_log(path, text, encoding=ENCODING):
    text = _get_log_text(text)
    print(text, flush=True)
    with open(str(path), 'a', encoding=encoding)as f:
        f.write(text + NEW_LINE)

def _get_log_text(text):
    # time_str = datetime.datetime.now().strftime('%y-%m-%d %H:%M:%S.%f    ')
    time_str = datetime.datetime.now().strftime('%F %H:%M:%S.%f    ')
    text = time_str + str(text) 
    return text


def wait_after_screenshot():
    time.sleep(0.15)

from selenium import webdriver
def _take_screenshot_driver(driver:webdriver.Chrome, logger:DriverLogger, add_file_name:str):
    # time_str = datetime.datetime.now().strftime('%F %H:%M:%S.%f')
    time_str = datetime.datetime.now().strftime('%F_%H_%M_%S_%f')
    file_name = time_str + '_{}.png'.format(add_file_name)
    image_path = logger.text_path.parent.joinpath(file_name)
    driver.save_screenshot(str(image_path))
    wait_after_screenshot()
    return image_path

def _save_page_source(driver:webdriver.Chrome, logger:DriverLogger, add_file_name:str, encoding=ENCODING):
    image_path = _take_screenshot_driver(driver, logger, add_file_name)
    file_name = image_path.stem + '.txt'
    page_source_path = image_path.parent.joinpath(file_name)
    with open(str(page_source_path), 'w', encoding=encoding)as f:
        f.write(driver.page_source)
    logger.put_log('save page_souce')
    logger.put_log('image = {}'.format(image_path))
    logger.put_log('page_source = {}'.format(page_source_path))
    return page_source_path

from selenium.webdriver.remote.webelement import WebElement
def get_attribute(element:WebElement, attribute:str):
    value = None
    try:
        value = element.get_attribute(attribute)
    except Exception as e:
        print(str(e))
    return value

class Rect():
    def __init__(self, start_x, start_y, end_x, end_y ) -> None:
        self.start_x = start_x
        self.left = start_x
        self.start_y = start_y
        self.top = start_y
        self.end_x = end_x
        self.right = end_x
        self.end_y = end_y
        self.bottom = end_y
        #/
        self.width = end_x - start_x
        self.height = end_y - start_y
        # 座標をタプルで定義
        self.top_left = self.left, self.top
        self.top_right = self.right, self.top
        self.bottom_left = self.left, self.bottom
        self.bottom_right = self.right, self.bottom
    def __str__(self):
        return f"[{self.left}, {self.top}] [{self.right}, {self.bottom}]"
    
import cv2
def _draw_rect_in_image(logger:DriverLogger, image_path, element:WebElement):
    el_rect = _get_rect_from_element(element)
    return _draw_rect_in_image_by_rect(logger, image_path, el_rect)

import shutil
def _draw_rect_in_image_by_rect(logger:DriverLogger, image_path, rect:Rect):
    if not Path(image_path).exists():
        msg = f"Error: '{image_path}' does not exist."
        logger.put_log(msg)
        raise FileNotFoundError(msg)
    else:
        msg = 'image_path = {}'.format(image_path)
        logger.put_log(msg)
        # 日本語文字が含まれる場合、imreadでエラーとなるかNoneとなるためファイル名をASCII文字のみにする
        file_name = datetime.datetime.now().strftime('%F_%H%M%S_draw_image.png')
        dist_path = Path(image_path).parent.joinpath(file_name)
        msg = 'copy_image dist_path = {}'.format(dist_path)
        logger.put_log(msg)
        shutil.copy(str(image_path), str(dist_path))
    # 画像を読み込む
    image_path = str(dist_path)
    # image_path[0] = image_path[0].upper()
    # image_path = image_path[0].upper() + image_path[1:]
    # image = cv2.imread(str(image_path).encode('utf-8'))
    image = cv2.imread(str(dist_path))
    if image is None:
        msg = "Failed to load image. Please check the image format and path."
        logger.put_log(msg)
        raise Exception(msg)
    image_shape_str = 'image_shape [{}, {}]'.format(image.shape[0], image.shape[1])
    logger.put_log(image_shape_str)
    # 枠を画像に描画する
    color = (147, 20, 255)  # BGR形式でピンク色
    thickness = 2  # 枠の太さ
    logger.put_log('rect.top_right = {}'.format(rect.top_left))
    logger.put_log('rect.top_left = {}'.format(rect.top_right))
    cv2.line(image, rect.top_left, rect.top_right, color, thickness)
    cv2.line(image, rect.top_right, rect.bottom_right, color, thickness)
    cv2.line(image, rect.bottom_right, rect.bottom_left, color, thickness)
    cv2.line(image, rect.bottom_left, rect.top_left, color, thickness)
    msg = 'element rect = {}'.format(rect)
    logger.put_log(msg)
    # dir_path = Path(image_path).parent
    # file_name = Path(image_path).stem + '_.png' 
    # write_image_file = dir_path.joinpath(file_name)
    cv2.imwrite(str(dist_path), image)
    msg = 'draw_rect = {}'.format(dist_path)
    logger.put_log(msg)



def _get_rect_from_element(element:WebElement):
    rect = element.rect
    left = rect['x']
    top = rect['y']
    right = left + rect['width']
    bottom = top + rect['height']
    # top_left = (rect['x'], rect['y'])
    # top_right = (rect['x'] + rect['width'], rect['y'])
    # bottom_left = (rect['x'], rect['y'] + rect['height'])
    # bottom_right = (rect['x'] + rect['width'], rect['y'] + rect['height'])
    rect = Rect(
        start_x=left,
        start_y=top,
        end_x=right,
        end_y=bottom)
    return rect

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import exceptions
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
def find_element_with_wait(logger:DriverLogger, driver:webdriver.Chrome, xpath_value:str, wait_time:float=10):
    msg = 'find by=xpath, value={}, wait={}'.format(xpath_value, wait_time)
    logger.put_log(msg)
    wait = WebDriverWait(driver, wait_time)  # Adjust the timeout to your needs
    element = None
    try:
        element = wait.until(EC.presence_of_element_located((By.XPATH, xpath_value)))
        # Now use 'element' to interact with the search box
        logger.put_log('found element')
    except exceptions.TimeoutException:
        logger.put_log("ページのロードを待つ時間がタイムアウトしました")
    return element

from selenium.webdriver.common.action_chains import ActionChains
def _input_text(driver:webdriver.Chrome, logger:DriverLogger, input_text):
    """ ActionChainsを使ってテキストボックスに文字列を入力 """
    actions = ActionChains(driver)
    # actions.click(input_box)  # 入力対象のテキストボックスをクリックしてフォーカスを当てる
    msg = '文字列を入力「{}」'.format(input_text)
    logger.put_log(msg)
    actions.send_keys(input_text)  # 文字列を入力
    # actions.send_keys(Keys.ENTER)  # エンターキーを送信
    actions.perform()  # アクションを実行
    image_path = _take_screenshot_driver(driver, logger, msg)



import os
def get_logger():
    import datetime
    date_str = datetime.datetime.now().strftime('%y%m%d_%H%M%S')
    log_dir = Path(__file__).parent.joinpath('__log' + date_str)
    log_dir.mkdir(exist_ok=True)
    # css_path = os.path.join(log_dir, 'log.css')
    # read_css_dir = Path(__file__).parent.joinpath('sample_files/log_sample1')
    # src_css_path = read_css_dir.joinpath(Path(css_path).name)
    log_text_path = log_dir.joinpath('text_log.log')
    logger = SimpleLogger()
    logger.init_parameter(log_text_path)
    return logger

def test_main():
    """
    selenium chromedriver テスト1

    URLにアクセスしてページのタイトルを取得するだけ
    """
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from webdriver_manager.chrome import ChromeDriverManager

    # ChromeDriverを自動でダウンロードし、初期化する
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    # Googleのホームページにアクセス
    driver.get("https://www.google.com")

    # ページのタイトルを出力
    print("ページのタイトルは:", driver.title)

    # ブラウザを閉じる
    driver.quit()
######################################################################

def test_main2():
    """
    selenium chromedriver テスト2

    URLにアクセスしてページのタイトルを取得するだけ
        Logger付き
    """
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from webdriver_manager.chrome import ChromeDriverManager
    #Loggerを取得する
    logger = get_logger()
    # ChromeDriverを自動でダウンロードし、初期化する
    logger.put_log('ChromeDriverを自動でダウンロードし、初期化する')
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    logger.put_log('created instance webdriver.Chrome')

    # Googleのホームページにアクセス
    logger.put_log('Googleのホームページにアクセス')
    url = 'https://www.google.com'
    logger.put_log('url = {}'.format(url))
    driver.get(url)

    # ページのタイトルを出力
    logger.put_log('ページのタイトルを出力')
    msg = "ページのタイトルは:", driver.title
    logger.put_log(msg)

    # ブラウザを閉じる
    logger.put_log('ブラウザを閉じる')
    driver.quit()
    logger.put_log('driver.quit executed')
    logger.put_log('logger_path = {}'.format(logger.path))
######################################################################
def test_main3():
    """
    selenium chromedriver テスト3

    URLにアクセスしてページのタイトルを取得するだけ
        Logger付き
         スクリーンショット付き
    """
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from webdriver_manager.chrome import ChromeDriverManager
    from selenium.webdriver.common.by import By
    #Loggerを生成する
    logger = get_logger()
    logger.put_log('Timerを生成する')
    timer = Timer()
    #/
    logger.put_log('ChromeDriverを自動でダウンロードし、初期化する')
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    logger.put_log('created instance webdriver.Chrome')
    #/
    logger.put_log('Googleのホームページにアクセス')
    url = 'https://www.google.com'
    logger.put_log('url = {}'.format(url))
    driver.get(url)
    timer.wait()
    #/
    logger.put_log('ページのタイトルを出力')
    msg = "ページのタイトルは:", driver.title
    logger.put_log(msg)
    #/
    logger.put_log('スクリーンショットを取得する')
    # # time_str = datetime.datetime.now().strftime('%F %H:%M:%S.%f')
    # time_str = datetime.datetime.now().strftime('%F_%H_%M_%S_%f')
    # file_name = time_str + '_スクリーンショットを保存.png'
    # image_path = logger.dir.joinpath(file_name)
    # driver.save_screenshot(str(image_path))
    image_path = _take_screenshot_driver(driver, logger, 'スクリーンショットを保存')
    logger.put_log('image_path = {}'.format(image_path))
    #/
    # driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
    driver.switch_to.frame(driver.find_element(By.XPATH ,"//iframe"))
    # フレーム内で要素を検索
    #/
    input_text = 'python selenium'
    input_text_search_box(driver, logger, input_text)
    # xpath_value = "//input[@name='q']"
    # # element = driver.find_element(By.XPATH, xpath_value)
    # element = find_element_with_wait(logger, driver, xpath_value)
    # _draw_rect_in_image(logger, image_path, element)
    #/
    logger.put_log('page_sourceを保存する')
    add_file_name = 'page_sourceを保存'
    _save_page_source(driver, logger, add_file_name)
    #/
    logger.put_log('ブラウザを閉じる')
    driver.quit()
    logger.put_log('executed driver.quit')
    #/
    logger.put_log('logger_path = {}'.format(logger.path))


from selenium.webdriver.common.keys import Keys
def input_text_search_box(driver:webdriver.Chrome, logger:DriverLogger, input_text:str):
    try:
        # 最初にフォーカスを設定するための要素を選択
        initial_element = driver.find_element(By.TAG_NAME, "body")
        initial_element.click()

        for i in range(10):
            # キーボードのタブキーを押す
            webdriver.ActionChains(driver).send_keys(Keys.TAB).perform()
            
            # 短い待機時間を設定
            time.sleep(1.5)
            
            # フォーカスが当たっているelementを取得
            active_element = driver.switch_to.active_element
            # print(active_element.tag_name)  # フォーカスが当たっているelementのタグ名を表示
            msg = 'activer_element.tag_name[{}] = {}'.format(i, active_element.tag_name)
            logger.put_log(msg)
            msg = 'activer_element.class[{}] = {}'.format(i, get_attribute(active_element, 'class'))
            logger.put_log(msg)
            msg = 'activer_element.id[{}] = {}'.format(i, get_attribute(active_element, 'id'))
            logger.put_log(msg)
            aria_role = active_element.aria_role
            msg = 'activer_element.aria_role[{}] = {}'.format(i, aria_role)
            logger.put_log(msg)
            rect = _get_rect_from_element(active_element)
            msg = 'activer_element.rect[{}] = {}'.format(i, rect)
            logger.put_log(msg)
            logger
            # タブを押しながら要素内を検索する
            # activer_element.aria_role = generic に変わったときが
            # 検索フォームにフォーカスが当たっている状態
            if aria_role=='generic':
                msg = '検索フォームを発見'
                image_path = _take_screenshot_driver(driver, logger, msg)
                _draw_rect_in_image(logger, image_path, active_element)
                break
        else:
            msg = 'aria_role == generic が見つからない'
            logger.put_log(msg)
    except Exception as e:
        raise e
    finally:
        # ドライバを閉じる
        # driver.quit()
        pass
        _input_text(driver, logger, input_text)
        actions = ActionChains(driver)
        logger.put_log('エンターキーを送信')
        actions.send_keys(Keys.ENTER)  # エンターキーを送信
        actions.perform()  # アクションを実行
        Timer().wait()
        logger.put_log('検索結果')
        image_path = _take_screenshot_driver(driver, logger, msg)
    return driver

def test_draw():
    logger = get_logger()
    image_dir_path = r'C:\Users\OK\source\repos\Repository4_python\scraping_test\selenium_utility\__log240425_062310'
    image_path_a = Path(image_dir_path).joinpath('2024-04-25_06_24_41_880054_文字列を入力「python selenium」.png')
    # image_path_b = Path(image_dir_path).joinpath('test.png')
    rect = Rect(100,100, 100,100)
    rect = Rect(100,100, 300,300)
    _draw_rect_in_image_by_rect(logger, image_path_a, rect)

if __name__ == '__main__':
    # test_main()
    # test_main2()
    test_main3()
    # test_draw()