from selenium.webdriver import ChromeOptions as Options
from selenium import webdriver

chrome_driver_path = r'C:\Users\OK\source\programs\chromedriver_win32\chromedriver'
options = Options()
options.add_argument('--disable-logging')
options.add_argument('--log-level=3')
options.add_experimental_option('excludeSwitches', ['enable-logging'])
# ブラウザを開く
driver = webdriver.Chrome(chrome_driver_path, options=options)
ChromeOptions = webdriver.ChromeOptions()
ChromeOptions.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome()
driver.get("https://www.google.co.jp")

import time
time.sleep(3)
print('done.')