
if __name__ == '__main__':
    import adb_common
    from  device_info import DeviceInfo
    from android_const import Constants
    from android_control_adb import AndroidControlAdb
else:
    # 外部から参照時は、common_util を sys.path へ追加しておくこと
    from common_util.adb_util import adb_common
    from common_util.adb_util.device_info import DeviceInfo
    from common_util.adb_util.android_const import Constants
    from common_util.adb_util.android_control_adb import AndroidControlAdb

class AndroidTransition():
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
        self.device_info = control_adb.device_info
        self.image_dir = image_dir
        self.control_adb = control_adb
        self.constants = Constants
    def initialize(self):
        self.logger.info(Constants.main.NOT_IMPLEMENTED.value)

    def to_home(self)->bool:
        try:
            flag = self.control_adb.input_keyevent(Constants.key.HOME.value)
            return flag
        except Exception as e:
            self.logger.exp.error(e)
            return False

    def to_settings(self)->bool:
        try:
            cmd = Constants.command.RUN_SETTINGS_MAIN.value
            flag ,ret_str = self.control_adb.excute_command_adb_shell(cmd)
            return flag
        except Exception as e:
            self.logger.exp.error(e)
            return False