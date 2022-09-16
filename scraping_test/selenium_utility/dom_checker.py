
if __name__ == '__main__':
    import pathlib,sys
    path = str(pathlib.Path(__file__).parent.parent)
    sys.path.append(path)

from movie_downloader_sub import DonwloadSite
from html_log.html_logger import HtmlLogger,BasicLogger
from selenium_webdriver.webdriver_utility import WebDriverUtility,WebElementUtility



def main():
    selenium_log_dir = r'C:\Users\OK\source\repos\test_media_files\selenium_log'
    log_dir_path = selenium_log_dir
    logger = BasicLogger(log_dir_path)
    logger.set_log_dir(log_dir_path,'image')
    check_url = DomChecker(None,logger)
    check_url.downloader_url = 'https://www.youtube.com/watch?v=LLfHddg2rbg'
    check_url.open_web_site()
    check_url.excute()
    return

class DomChecker(DonwloadSite):
    def __init__(self, chrome_driver_path: str, html_logger: HtmlLogger) -> None:
        super().__init__(chrome_driver_path, html_logger)
        self.bar = '############################################################'
    def excute(self):
        #タブキーでずらして、選択する
        #終了するときはデバッグコンソールで
        flag = True
        while(flag):
            element = self.chrome.driver.switch_to.active_element
            elu = WebElementUtility(element)
            print() #break
            print(self.bar)
            print(elu.print_attributes_for_analyze())
            self.chrome.timer.wait(3)
        print('EXIT')
    def print_analyze(self):
        print()
        print(self.bar)

if __name__ == '__main__':
    main()