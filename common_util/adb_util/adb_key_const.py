
from enum import Enum

class keycoce_const:
    HOME = 'KEYCODE_HOME'
    POWER = 'KEYCODE_POWER'

class const_command:
    GET_PACKAGE_LIST = 'adb shell pm list packages'
    SCREEN_CAPTURE_TO_SD = 'screencap -p /sdcard/capture.png'
    BLUETOOTH_OFF_ON = 'am start -a android.bluetooth.adapter.action.REQUEST_ENABLE'
    RUN_SETTINGS_WIFI = 'am start -n com.android.settings/.wifi.WifiSettings'
    GET_WIFI_INFO = 'am start -n com.android.settings/.wifi.WifiInfo'
    GET_WIFI_STATUS = 'am start -n com.android.settings/.wifi.WifiStatusTest'
    RUN_SETTINGS_LANGUAGE = 'am start -n com.android.settings/.LanguageSettings'
    RUN_SETTINGS_DEVELOPMENT = 'am start -n com.android.settings/.DevelopmentSettings'
    RUN_SETTINGS_DATETIME = 'am start -n com.android.settings/.DateTimeSettingsSetupWizard'
"""
※Keyevent 一例
KEYCODE_HOME	ホーム キー
KEYCODE_BACK	バック(戻る)キー
KEYCODE_CAMERA	カメラキー
KEYCODE_COPY	コピーキー
KEYCODE_PASTE	ペーストキー
KEYCODE_POWER	電源ボタン　(起動状態ならスリープ、スリープ中なら復帰)
KEYCODE_SLEEP	スリープ (スリープ中に再実行しても何も起きない)
KEYCODE_WAKEUP	スリープ解除 (起動状態で再実行しても何も起きない)
"""