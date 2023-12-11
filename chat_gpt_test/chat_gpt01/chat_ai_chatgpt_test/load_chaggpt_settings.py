
_INFO_DIR_PATH = r'C:\Users\OK\source\repos\test_media_files\_test_info'

from pathlib import Path
class ChatGptSetting():
    def __init__(self) -> None:
        pass
    def get_chat_api_key(self):
        path = Path(_INFO_DIR_PATH).joinpath('chag_gpt_api_key.txt')
        return self.get_file_content(path)
        
    def get_file_content(self, path):
        with open(str(path), 'r', encoding='utf-8')as f:
            buf = f.read()
        return buf

chatgpt_settting = ChatGptSetting()

class CookieKeys():
    API_KEY = 'ApiKey'


