# from bardapi import BardCookies
from bardapi import Bard
import load_chrome_token 
from load_chrome_token import CookieKeys

cookie_dict = load_chrome_token.cookie_dict

bard = None
try:
    # bard = BardCookies(cookie_dict=cookie_dict)
    token = cookie_dict[CookieKeys.PSID]
    print('token = {}'.format(token))
    bard = Bard(token=token)
except Exception as e:
    # Exception: SNlM0e value not found in response. Check __Secure-1PSID value.
    if 'Check __Secure-1PSID value' in str(e):
        print('ERROR:{}'.format(str(e)))
        print('cookie_dict __Secure-1PSID = {}'.format(cookie_dict[CookieKeys.PSID]))
    else:
        raise e
if bard == None:
    print('* bard == None')
    exit(0)

prompt="LLMとはなんですか?"
prompt="LLMサービスがいくつかあると思いますが、できる限りの数を列挙してください。"
response = bard.get_answer(prompt)['content']
print('======')
print('prompt = {}'.format(prompt))
print('======')
print('response =')
print(response)