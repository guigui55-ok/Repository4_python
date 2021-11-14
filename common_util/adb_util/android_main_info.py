

import adb_util
from adb_util import adb_key
from adb_util.adb_key_const import keycoce_const
from adb_util.android_const import const as android_const
from adb_util.android_const import const_int as android_const_int
from adb_util.android_const import const_screen_image_file_names as const_images
from adb_util.android_const import const_state as const_state
from adb_util import adb_common

class android_info():
    logger = None
    const_android : android_const= None
    const_screen_image_file_names : const_images= None
    def __init__(self,logger) -> None:
        self.logger = logger
        self.android_const = android_const
        self.const_screen_image_file_names = const_images
        adb_util.logger = self.logger
    
    def get_package_list(
        self,
        package_name_filter : str = '',
        option : str = '' ,
        device_id : str = '',
        is_logout_stdout : bool = True
    ) -> str:
        """
            -f	apkのパスとパッケージ名を表示\n
            -d	無効にしたアプリをフィルタ表示\n
            -e	無効にしていないアプリをフィルタ表示\n
            -s	システムアプリをフィルタ表示\n
            /system/apps または /system/priv-apps のアプリ\n
            -3	3rdパーティ製アプリをフィルタ表示\n
            ユーザーがインストールしたアプリ\n
            -i	インストーラーを表示\n
            -u	アンインストールされたパッケージを含むアプリを表示\n
            アップデート済みのアプリ\n
            --user <USER_ID>	ユーザIDによるフィルタ表示\n
            adb shell pm list packages -f | sort / sort コマンドと組み合わせて使用すると見やすく\n
        """
        try:
            from adb_util.adb_common import get_info_package_list
            ret = get_info_package_list(package_name_filter,option,device_id,is_logout_stdout)
            return ret
        except Exception as e:
            self.logger.exp.error(e)
            return ''

