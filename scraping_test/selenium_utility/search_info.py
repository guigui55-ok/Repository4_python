


########################################################################

class ConstPlatform():
    """ 実行するPCの環境 """
    WINDOWS = 1
    LINUX = 2
    MAC = 3

class ConstSearchInfo():
    """ search_info.py で使用する定数 """
    # 240416 以下にいろいろ小分けにした定数クラスがあるが、わかりにくいのでこのクラスで一元管理する。
    # 使用目的をPrefixに付与している。
    #/
    # 検索時のデータの種類
    # 他に、list,single_data,avgなどを想定している（検討中）
    SEARCH_DATA_TYPE_STRING = 0
    SEARCH_DATA_TYPE_NUMBER = 1
    #/
    # 検索の結果判定方法
    # いくつ探して、いくつヒットしたら合致、 ヒットしたものすべて、などを想定しています
    MATCH_CONDITIONS_PERFECT = 1
    MATCH_CONDITIONS_PART = 2
    MATCH_CONDITIONS_ANY = 3
    MATCH_CONDITIONS_ALL= 4
    MATCH_CONDITIONS_FIRST_ONLY = 5
    #/
    # Seleniumを実行するPCの環境
    PLATFORM_WINDOWS = 1
    PLATFORM_LINUX = 2
    PLATFORM_MAC = 3
    class ConstPlatform(ConstPlatform):
        """ 実行するPCの環境 """
        pass
    #/
    # 検索する対象のもの、検索時にメインで使用するもの
    SEARCH_TARGET_WEB = 1
    SEARCH_TARGET_DATABASE = 2
    SEARCH_TARGET_FILE_MANAGER = 3
    SEARCH_TARGET_FILE_CONTENT = 4
    SEARCH_TARGET_FILE_EXCEL = 5
    SEARCH_TARGET_FILE_TEXT = 6
    SEARCH_TARGET_EXCEL_VALUE = 10
    #/
    # 検索時に使用するアプリ名
    APP_NAME_BROWSER_CHROME = 1
    APP_NAME_BROWSER_FIREFOX = 2
    APP_NAME_EXPLORER = 10

########################################################################
class DataType():
    STRING = 1
    NUMBER = 2
    # list,single_data,avg

class MatchConditions():
    NONE = 0
    PERFECT = 1
    # いくつ探して、いくつヒットしたら合致
    # ヒットしたものすべて

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
    """
    何かを検索するときに使用するクラス
    """
    def __init__(self, value:str='') -> None:
        self.data_type = ConstSearchInfo.SEARCH_DATA_TYPE_STRING
        self.data_value = value
        self.platform = ConstPlatform.WINDOWS
        self.match_conditions = ConstSearchInfo.MATCH_CONDITIONS_PERFECT
        self.search_target = ConstSearchInfo.SEARCH_TARGET_WEB
        self.app_kind = ConstSearchInfo.APP_NAME_BROWSER_CHROME

from abc import ABCMeta, abstractmethod
class AbstractSearchInfomations(metaclass=ABCMeta):
    """多くのデータから何かを検索するクラス"""

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