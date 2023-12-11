# from bardapi import BardCookies
from bardapi import Bard
import load_chrome_token 
from load_chrome_token import CookieKeys
from pathlib import Path

cookie_dict = load_chrome_token.cookie_dict

class ChatAiBard():
    def __init__(self, token='') -> None:
        self.token:str = token
        self.chat_ai:Bard = None
        self.debug_print:bool = True
        self.w_buf_list:'list[str]' = []
    
    def _is_invalid_token(self):
        if self.token == '':
            raise Exception('token is invalid (token={})'.format(self.token))

    def create_ai_instance(self):
        try:
            self._print('token = {}'.format(self.token))
            self.chat_ai = Bard(token=self.token)
        except Exception as e:
            # Exception: SNlM0e value not found in response. Check __Secure-1PSID value.
            if 'Check __Secure-1PSID value' in str(e):
                self._print('ERROR:{}'.format(str(e)))
                self._print('cookie_dict __Secure-1PSID = {}'.format(cookie_dict[CookieKeys.PSID]))
            else:
                raise e
        if self.chat_ai == None:
            self._print('* bard == None')
            return
        
    def _print(self, value):
        if self.debug_print:
            print(value)

    def _test_get_response_write_text(self, prompt:str):
        self._append_w_buf('======') 
        self._append_w_buf('prompt = {}'.format(prompt)) 
        self._append_w_buf('======') 
        self._append_w_buf('response =') 
        response = self.chat_ai.get_answer(prompt)['content']
        self._append_w_buf(response)
        self._print(''.join(self.w_buf_list))
        ###
        w_path = Path(r'C:\Users\OK\source\repos\test_media_files\_chat_ai')
        w_path.mkdir(exist_ok=True)
        import datetime
        file_name = 'bard_' + datetime.datetime.now().strftime('%y%m%d_%H%M%S') + '.txt'
        w_path = w_path.joinpath(file_name)
        with open(str(w_path), 'w', encoding='utf-8')as f:
            f.writelines(self.w_buf_list)
        self._print('======')
        self._print('w_path = {}'.format(w_path))

    def _append_w_buf(self, buf):
        _NEW_LINE = '\n'
        self.w_buf_list.append(buf + _NEW_LINE)

if __name__ == '__main__':
    token = cookie_dict[CookieKeys.PSID]
    # token = 'tjdj qluj vzjc kiqr'
    bard = ChatAiBard(token=token)
    bard.create_ai_instance()
    prompt = ''
    # prompt="LLMとはなんですか?"
    # prompt="LLMサービスがいくつかあると思いますが、できる限りの数を列挙してください。"
    # prompt='以下のソースコードで悪いところ、改善すべきトロがあれば直していただけますか？'
    # prompt+='\n-----------------\n'
    # with open(__file__, 'r', encoding='utf-8')as f:
    #     prompt+=f.read()
    # prompt='pythonでbardapiを私用するとき以下のエラーが発生することがあります。これを発生させたくないのですがどのようにしたらよいでしょうか？\n'
    # prompt+="エラー：Exception: SNlM0e value not found. Double-check __Secure-1PSID value or pass it as token='xxxxx'."
    # prompt = 'Googleアカウント設定の「アプリ パスワード」で生成されたパスワードを、pythonのbardapiのトークンとして使用できますか？'
    # prompt = '以下の英語を日本語に翻訳してください。\n'
    # prompt += "Exception: SNlM0e value not found. Double-check __Secure-1PSID value or pass it as token='xxxxx'."
    # 231209
    # 上記エラーとなってしまうときは、ブラウザにBardページを閉じたほうが良い？
    if prompt == '' or prompt == None:
        bard._print('prompt == Nothing')
        exit(0)
    bard._test_get_response_write_text(prompt)
