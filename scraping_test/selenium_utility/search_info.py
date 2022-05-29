
class DataType():
    STRING = 1
    NUMBER = 2
    # list,single_data,avg

class MatchConditions():
    NONE = 0
    PERFECT = 1
    # いくつ探して、いくつヒットしたら合致
    # ヒットしたものすべて

class Platform():
    WINDOWS = 1
    LINUX = 2
    MAC = 3

class SearchTarget():
    WEB = 1
    DATABASE = 2
    FILE_MANAGER = 3
    FILE_EXCEL = 4
    FILE_TEXT = 5

class BrowserKind():
    CHROME = 1
class AppKind():
    browser = BrowserKind()
    def __init__(self) -> None:
        pass

class TaargetDataInfo():
    def __init__(self,value:str='') -> None:
        self.data_type = DataType.STRING
        self.data_value = value
        self.platform = Platform.WINDOWS
        self.match_conditions = MatchConditions.PERFECT
        self.search_target = SearchTarget.WEB
        self.app_kind = AppKind.browser.CHROME

from abc import ABCMeta, abstractmethod
class AbstractSearchInfomations(metaclass=ABCMeta):
    """多くのデータから何かを検索する仕組み"""

    def __init__(self,target_data_info:TaargetDataInfo) -> None:
        self.target = target_data_info
        self.log_dir:str = ''
    
    # @abstractmethod
    def set_log_dir(self,dir:str):
        import os
        if not os.path.exists(dir):
            os.mkdir(dir)
        else:
            if os.path.isfile(dir):
                os.remove(dir)
                os.mkdir(dir)
        self.log_dir = dir

    @abstractmethod
    def prepare_data(self,dir:str):
        pass

    @abstractmethod
    def run_app(self):
        pass

    @abstractmethod
    def trandition_input_screen(self):
        pass

    @abstractmethod
    def input_data(self):
        pass

    @abstractmethod
    def get_result(self):
        pass
    
    @abstractmethod
    def get_result(self):
        pass
    
    @abstractmethod
    def align_result(self):
        pass
    
    @abstractmethod
    def analyze_result(self):
        pass

    @abstractmethod
    def determine_if_values_match(self):
        """値が一致しているか判定する determine if the values match"""
        pass