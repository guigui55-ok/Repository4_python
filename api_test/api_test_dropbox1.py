import dropbox
import dropbox.dropbox_client
import dropbox.file_requests
import requests
import api_info_reader
from custom_logger import CustomLogger as Logger


def test_main():
    logger = Logger()
    logger.info("\n*****")

    ACCESS_TOKEN = 'xxx'
    REFRESH_TOKEN = api_info_reader.get_refresh_token()
    APP_KEY = api_info_reader.get_api_key()
    APP_SECRET = api_info_reader.get_security_key()

    #確認ですが、リフレッシュトークンはwww.dropbox.com/oauth2/authorize自体から返される値ではありません。
    # www.dropbox.com / oauth2/authorize で「response_type=code」を指定すると、
    # 「認証コード」（「アクセスコード」と呼ばれることもあります）が返されます。

    # refreshToken の値は、/oauth2/ tokenを 'grant_type=authorization_code' で呼び出した際に返される 'refresh_token' である必要があります。これは 'access token' や 'authorization code' とは異なり、これら 3 つは互換性がありません。


    #「リフレッシュトークン」を利用してアクセストークン取得
    auth = (APP_KEY, APP_SECRET)
    param = {
        'grant_type': 'refresh_token', 
        'refresh_token': REFRESH_TOKEN}
    url = 'https://api.dropboxapi.com/oauth2/token'

    logger.info("url = {}".format(url))
    logger.info("auth = {}".format(auth))
    logger.info("param = {}".format(param))

    res = requests.post(url, auth=auth, data=param)

    # 結果を出力
    logger.info("Response code:"+ str(res.status_code))
    logger.info("Response body:"+ str(res.text))

    if res.status_code != 200:
        res.raise_for_status()

    token = res.json()
    logger.info("token = {}".format(token))

    dbx = dropbox.Dropbox(token['access_token'])

    #「チームスペース」対応
    root_namespace_id = dbx.users_get_current_account().root_info.root_namespace_id
    dbx = dbx.with_path_root(dropbox.common.PathRoot.root(root_namespace_id))

if __name__ == '__main__':
    test_main()