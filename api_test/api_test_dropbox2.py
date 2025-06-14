#https://zerofromlight.com/blogs/detail/124/

import requests
import api_info_reader
from custom_logger import CustomLogger as Logger

from dropbox import DropboxOAuth2FlowNoRedirect


def test_main():
    logger = Logger()
    logger.info("\n*****")
    
    REFRESH_TOKEN = api_info_reader.get_refresh_token()
    APP_KEY = api_info_reader.get_api_key()
    APP_SECRET = api_info_reader.get_security_key()

    auth_flow = DropboxOAuth2FlowNoRedirect(
                            APP_KEY,
                            consumer_secret=APP_SECRET, # PKCEがFalseの場合に必要
                            use_pkce=False, # Trueだとシークレットキーは不要
                            token_access_type='offline'
    )
    auth_flow.start()
    logger.info(str(type(auth_flow)))
    logger.info(str(auth_flow))

    oauth_result = auth_flow.finish('認証コード')
    logger.info('oauth_result = {}'.format(oauth_result))
    refresh_token = oauth_result.refresh_token
    logger.info('refresh_token = {}'.format(refresh_token))
    

if __name__ == '__main__':
    test_main()