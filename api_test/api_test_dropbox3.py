#https://zerofromlight.com/blogs/detail/122/

import requests
import api_info_reader
from custom_logger import CustomLogger as Logger

import dropbox
"""
DropBox設定
App folder
files.content.write
files.content.read

"""

def test_main():
    logger = Logger()
    logger.info("\n*****")

    ACCESS_TOKEN = api_info_reader.get_access_token()
    logger.info('ACCESS_TOKEN = {}'.format(ACCESS_TOKEN))
    
    # 対象のDropboxフォルダパス（ルートなら '' または '/'）
    DROPBOX_FOLDER_PATH = ''  # 例: "/uploaded" または "/" など
    #Dropbox APIでは「ルートフォルダ」を指定するときに / ではなく、空文字列 '' を使う必要があります。


    dbx = dropbox.Dropbox(ACCESS_TOKEN)
    
    try:
        result = dbx.files_list_folder(DROPBOX_FOLDER_PATH)
        logger.info(f"📂 フォルダ: {DROPBOX_FOLDER_PATH} のファイル一覧:")
        logger.info("len result.entries = {}".format(len(result.entries)))
        for entry in result.entries:
            logger.info(f"- {entry.name}")
        
        # 続きがある場合（ページング対応）
        while result.has_more:
            result = dbx.files_list_folder_continue(result.cursor)
            for entry in result.entries:
                logger.info(f"- {entry.name}")

        logger.info(" ###### ")        
        logger.info(type(dbx))
        logger.info("users_get_current_account = ")
        logger.info(dbx.users_get_current_account())
        logger.info("users_get_current_account = " + str(dbx.users_get_current_account().email))
        # logger.info("files_list_folder = ")
        # logger.info(dbx.files_list_folder(''))

    except dropbox.exceptions.ApiError as err:
        print(f"❌ エラーが発生しました: {err}")


    
if __name__ == '__main__':
    test_main()