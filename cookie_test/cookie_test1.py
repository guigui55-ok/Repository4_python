# https://qiita.com/shinkai_/items/090fb79d297a30001a86

import requests

# URLから、requestsのオブジェクト作成
url = "https://qiita.com"
url = 'https://bard.google.com/chat'
session = requests.session()
response = session.get(url)
print('response = {}'.format(response)) # <Response [200]>

# cookieを取得
cookie = response.cookies
print('cookie = {}'.format(cookie))
"""
cookie = <RequestsCookieJar[<Cookie _qiita_login_session=Za7N8ouWQ9m%2BY6zrVcuhvxaXUJqT51MF3AEVGqzNqDXm0S4rDQVTUWDDMLO%2BG0jn48DNj4qVTV6%2BirPzL7sD6AqzQXXqmlW0IUHKR2QL7pGbDtvgTi5wJZfL7RdkkiH0bbRRuBj%2FcsaPk8v2DIz9Z%2FY1R0WqTXpYvt9nOSaIMVpOzuv0DyCRP4AirghZGOpme%2FMAWNubt%2BRcphuBi3P21jzVqLgfBDPB8NXzg1QInYzZzIe4ZLMbSXH91XKWQ%2FURStgT3heAwwG64wfkDnh0YcSCASENbCdiaYEHfuW1aQvM0qxzWMBmaMNv2l0EmVEqaoY2sk%2BHIJbe25Kafcp1JCYFsYUsWydPVfm%2B00pF--LbeicWNupqRQmIlP--2dOW6XJjywTaVNYlD%2BKVnA%3D%3D for .qiita.com/>]>
"""

# cookie内の任意項目を指定して取得
item  = response.cookies.get('_qiita_login_session')
print('item = {}'.format(item))
"""
item = FWdBf597iilLTNYUnqnwhXBvZbjcrBaqW5t7GUoXK2mGPYeQJ3YktVfWu3fsVECO1ziV5Y85pgFnhLs8WVxBDpqHxZ9BICdH08U5FZpIIgrZz3aMMm2N3uL3rqFvx3NHVA53ZCl5%2BHKaA2tM06%2F6x9f9USIDKPw%2BLK%2Fpi1pihHRKuG%2F1ML3RNYCFpmWM%2Fbt0EP8XACjIB4DjBmwVa5OsiwxCsLDecgKT4luwl2x7TTHT%2F0fnyhexr44anzl%2Bq1k29fczdRvzn7O0ppgT7FWE2zBHpqQKvLkIWxmeL0SGqtXKCfpOGO9VFvG9EPIx2j%2BHBOdaWAiPdoCF8dVErfFE3GCVV%2B791bb46II%2BcQp9--LqJzrrdf2O%2BhZiu%2F--hw2nVOAlHyGCaK4ApCcfTQ%3D%3D
"""

