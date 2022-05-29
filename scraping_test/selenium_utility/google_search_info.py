from search_info import AbstractSearchInfomations,TaargetDataInfo

# class TaargetDataInfo():
#     def __init__(self,value:str='') -> None:
#         self.data_type = DataType.STRING
#         self.data_value = value
#         self.platform = Platform.WINDOWS
#         self.match_conditions = MatchConditions.PERFECT
#         self.search_target = SearchTarget.WEB
#         self.app_kind = AppKind.browser.CHROME

GOOGLE_URL = 'https://www.google.co.jp/'


from selenium_webdriver.webdriver_utility import WebDriverUtility

class SearchInfoByGoogle(AbstractSearchInfomations):
    """Googleから情報を検索する"""

    def __init__(self,target_data_info:TaargetDataInfo,web_driver_path:str) -> None:
        self.target:TaargetDataInfo = target_data_info
        self.web_deiver_path = web_driver_path
        self.log_dir = ''
    
    def set_log_dir(self,dir:str):
        super().set_log_dir(dir)
    
    def prepare_data(self):
        pass

    def run_app(self):
        self.chrome = WebDriverUtility(self.web_deiver_path)
        self.chrome.driver.get(GOOGLE_URL)
        self.chrome.selenium_log.set_log_dir(self.log_dir)

    def trandition_input_screen(self):
        pass

    def input_data(self):
        search_bar = self.chrome.driver.find_element_by_name("q")
        search_bar.send_keys(self.target.data_value)
        search_bar.submit()

    def get_result(self):
        self.chrome.screenshot()
        self.chrome.write_page_source()
        for elem_h3 in self.chrome.driver.find_elements_by_xpath('//a/h3'):
            elem_a = elem_h3.find_element_by_xpath('..')
            print(elem_h3.text)
            print(elem_a.get_attribute('href'))
        
    def align_result(self):
        pass
    
    def analyze_result(self):
        pass

    def determine_if_values_match(self):
        """値が一致しているか判定する determine if the values match"""
        pass


def test_main():
    target_data = TaargetDataInfo('python')
    w_path = r'C:\Users\OK\source\programs\chromedriver_win32\chromedriver'
    google_searcher = SearchInfoByGoogle(target_data,w_path)
    import pathlib
    google_searcher.set_log_dir(str(pathlib.Path(__file__).parent.joinpath('log')))
    google_searcher.run_app()
    google_searcher.input_data()
    google_searcher.get_result()
    google_searcher.chrome.close()

if __name__ == '__main__':
    test_main()