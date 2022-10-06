
##########
import sys
# library base path
path = 'C:\\Users\\OK\\source\\repos\\Repository4_python'
sys.path.append(path)
##########
import scraping_test
print(str(scraping_test.__path__[0]))
sys.path.append(str(scraping_test.__path__[0]))
import scraping_test.selenium_utility as selenium_utility
print(selenium_utility.__path__[0])
sys.path.append(selenium_utility.__path__[0])

from selenium_utility import selenium_webdriver
print(selenium_webdriver.__path__)
sys.path.append(selenium_webdriver.__path__)

from scraping_test.selenium_utility.selenium_webdriver.webdriver_utility import WebDriverUtility
