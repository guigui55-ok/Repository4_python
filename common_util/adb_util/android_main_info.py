

if __name__ == '__main__':
    import adb_common
    from  device_info import DeviceInfo
    from android_const import Constants
    from android_control_adb import AndroidControlAdb
else:
    # 外部から参照時は、common_util,adb_util を sys.path へ追加しておく
    import adb_util.adb_common as adb_common
    from  adb_util.device_info import DeviceInfo
    from adb_util.android_const import Constants
    from adb_util.android_control_adb import AndroidControlAdb


class AndroidInfo():
    logger = None
    constants : Constants
    image_dir = None
    device_info : DeviceInfo
    control_adb : AndroidControlAdb

    def __init__(
        self,
        logger,
        control_adb :AndroidControlAdb,
        image_dir : str
    ) -> None:
        self.logger = logger
        self.control_adb = control_adb
        self.device_info = control_adb.device_info
        self.image_dir = image_dir
        self.constants = Constants
    

    
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
            ret = adb_common.get_info_package_list(package_name_filter,option,device_id,is_logout_stdout)
            return ret
        except Exception as e:
            self.logger.exp.error(e)
            return ''

