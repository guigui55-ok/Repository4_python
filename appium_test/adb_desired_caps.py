
import adb.adb_main as adb_main

def create_desired_caps_for_android(
    package:str, activity:str):
    desired_caps = {}
    # desired_caps['automationName'] = 'UiAutomator2'
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = adb_main.get_android_version()
    desired_caps['deviceName'] = adb_main.get_device_product_model()
    desired_caps['appPackage'] = package
    desired_caps['appActivity'] = activity
    return desired_caps