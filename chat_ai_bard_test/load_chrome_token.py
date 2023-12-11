
_INFO_DIR_PATH = r'C:\Users\OK\source\repos\test_media_files\_test_info'

from pathlib import Path
class ChromeToken():
    def __init__(self) -> None:
        pass
    def get_secure_1PSID(self):
        path = Path(_INFO_DIR_PATH).joinpath('chrome_1PSID.txt')
        return self.get_file_content(path)
    
    def get_secure_1PSIDTS(self):
        path = Path(_INFO_DIR_PATH).joinpath('chrome_1PSIDTS.txt')
        return self.get_file_content(path)
    
    def get_secure_1PSIDCC(self):
        path = Path(_INFO_DIR_PATH).joinpath('chrome_1PSIDCC.txt')
        return self.get_file_content(path)
    
    def get_secure_1PAPISID(self):
        path = Path(_INFO_DIR_PATH).joinpath('chrome_1PAPISID.txt')
        return self.get_file_content(path)
    
    def get_file_content(self, path):
        with open(str(path), 'r', encoding='utf-8')as f:
            buf = f.read()
        return buf

chrome_token = ChromeToken()

class CookieKeys():
    PSID = '__Secure-1PSID'
    PSIDDTS = '_Secure-1PSIDTS'
    PSIDCC = '__Secure-1PSIDCC'
    PAPISID = '__Secure-1PAPISID'

cookie_dict = {
    CookieKeys.PSID : chrome_token.get_secure_1PSID(),
    CookieKeys.PSIDDTS: chrome_token.get_secure_1PSIDTS(),
    CookieKeys.PSIDDTS: chrome_token.get_secure_1PSIDCC(),
    CookieKeys.PAPISID: chrome_token.get_secure_1PAPISID()
}



buf = ''