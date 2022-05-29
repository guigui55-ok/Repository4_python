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
from time import sleep

def main():
    path = r'C:\Users\OK\source\programs\chromedriver_win32\chromedriver'
    driver = webdriver.Chrome(path)
    # driver = webdriver.Chrome()
    """
        raise WebDriverException(
selenium.common.exceptions.WebDriverException: Message: 'chromedriver' executable needs to be in PATH. Please see https://sites.google.com/a/chromium.org/chromedriver/home
    """
    print(driver)
    print()
    print('-----')
    driver.get('https://www.google.co.jp/')
    search_bar = driver.find_element_by_name("q")
    search_bar.send_keys("python")
    search_bar.submit()

    
    for elem_h3 in driver.find_elements_by_xpath('//a/h3'):
        elem_a = elem_h3.find_element_by_xpath('..')  
        print(elem_h3.text)
        print(elem_a.get_attribute('href'))

main()