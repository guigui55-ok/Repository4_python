"""

https://yuki.world/python-selenium-chromedriver-auto-update/
"""


from selenium import webdriver
import chromedriver_binary

def main():
    path = r'C:\Users\OK\source\programs\chromedriver_win32\chromedriver'
    # driver = webdriver.Chrome(path)
    driver = webdriver.Chrome()
    """
        raise WebDriverException(
selenium.common.exceptions.WebDriverException: Message: 'chromedriver' executable needs to be in PATH. Please see https://sites.google.com/a/chromium.org/chromedriver/home
    """
    print(driver)

main()