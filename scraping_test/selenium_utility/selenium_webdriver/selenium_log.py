
import pathlib
class SeleniumLogger():
    def __init__(self,log_dir:str='') -> None:
        if log_dir == '':
            path = str(pathlib.Path(__file__).parent.parent.joinpath('log'))
            log_dir = path
        self.set_log_dir(log_dir)
    def set_log_dir(self,dir:str):
        import os
        if not os.path.exists(dir):
            os.mkdir(dir)
        else:
            if os.path.isfile(dir):
                os.remove(dir)
                os.mkdir(dir)
        self.log_dir = dir



import os
import sys
from selenium.webdriver.chrome.options import Options

from selenium import webdriver
def screenshot(driver:webdriver.Chrome,image_file_path:str):

    # File Name
    # FILENAME = os.path.join(os.path.dirname(os.path.abspath(__file__)), "image/screen.png")

    # set driver and url
    # driver = webdriver.Chrome('./chromedriver')
    # url = 'https://www.rakuten.co.jp/'
    # driver.get(url)

    # get width and height of the page
    w = driver.execute_script("return document.body.scrollWidth;")
    h = driver.execute_script("return document.body.scrollHeight;")
    # set window size
    driver.set_window_size(w,h)
    # Get Screen Shot
    driver.save_screenshot(image_file_path)

    # Close Web Browser
    # driver.quit()