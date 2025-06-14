import requests
import api_info_reader
from custom_logger import CustomLogger as Logger

def test_download():
    url='https://content.dropboxapi.com/2/files/download'
    filename='test_file_name'

    urlData = requests.get(url).content

    with open(filename ,mode='wb') as f: # wb でバイト型を書き込める
        f.write(urlData)

def test_main():
    logger = Logger()
    logger.info("\n*****")

    ACCESS_TOKEN = api_info_reader.get_access_token()
    API_KEY = api_info_reader.get_api_key()
    SECURITY_KEY = api_info_reader.get_security_key()

    # url = 'https://api.dropboxapi.com/oauth2/token'
    # data = {
    #     'grant_type' : 'refresh_token',
    #     'refresh_token' : REFRESH_TOKEN,
    # }

    # #アクセストークン取得
    # url = "https://api.dropbox.com/oauth2/token"
    # data = {
    #     'code' : ACCESS_TOKEN,
    #     'grant_type' : "authorization_code",
    #     API_KEY : SECURITY_KEY
    # }

    # リフレッシュトークン取得
    url = "https://api.dropbox.com/oauth2/token"
    data = {
        'code' : ACCESS_TOKEN,
        'grant_type' : "authorization_code",
        API_KEY : SECURITY_KEY
    }

    logger.info("url = {}".format(url))
    logger.info("data = {}".format(data))
    response = requests.get(url, params=data)

    # 結果を出力
    logger.info("Response code:"+ str(response.status_code))
    logger.info("Response body:"+ str(response.text))

###############################
import subprocess
def run_curl(logger:Logger,  request_url ):

    # curlコマンドを定義
    curl_command = [
        "curl",
        "-X", "GET",  # HTTPメソッド
        request_url,  # リクエストURL
    ]

    # subprocessでcurlコマンドを実行
    result = subprocess.run(curl_command, capture_output=True, text=True)

    # 結果を出力
    logger.info("Response code:", result.returncode)
    logger.info("Response body:", result.stdout)

# GET以外も使い方は同じ。

# r = requests.post(url)
# r = requests.put(url)
# r = requests.delete(url)

# レスポンス

# サーバからのレスポンスは、レスポンスの形式に応じて以下のように確認できます。

# # テキスト
# r.text

# # バイナリ
# r.content

# # JSON
# r.json()

# # 生レスポンス
# r.raw

# # レスポンスのHTTPステータスコード
# r.status_code

if __name__ == '__main__':
    test_main()
    