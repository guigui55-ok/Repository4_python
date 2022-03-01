
import import_init
import traceback

debug_mode = True

def test_adb_com():
    try:
        import common_utility.adb_util.adb_common as adb_com

        # ###
        # cmd = 'adb devices'
        # result = adb_com.get_result_subprocess_run_command(cmd)
        # adb_com.logout_result_subprocess_run_text(result)

        # ###
        # cmd = 'adb shell input touchscreen tap 100 100'
        # result = adb_com.adb_shell_with_show_result(cmd)
        # adb_com.logout_result_subprocess_run_text(result)

        # ###
        # flag = adb_com.is_success_adb_result(result,'message',True)

        # ###
        # path = adb_com.screen_capture_for_android()
        # print('screen_capture_for_android , path = ' + path)
        # flag = adb_com.save_file_from_android(path)
        # print('screen_capture_for_android , flag = ' + str(flag))
        # flag = adb_com.save_file_to_pc_from_android()
        # print(flag)
        
        # ###
        # path = adb_com.screen_record()
        # print('screen_record , path = ' + path)
        # flag = adb_com.save_file_from_android(path)
        # print('screen_record , flag = ' + str(flag))

        # ###
        # flag = adb_com.adb_reboot()
        # print('adb_reboot , flag = ' + str(flag))

        # ###
        # adb_com.get_result_adb_shell_by_poppen('')

        # adb_com.start_package('package_name','activity_name')

        # ###
        # flag = adb_com.input_text('input')
        # print('input_text , flag = ' + str(flag))

        # ###
        # rect = [0,0,500,500]
        # point = adb_com.get_center_from_rect(rect)
        # print('get_center_from_rect , flag = ' + str(point))

        # ###
        # rect = [0,0,500,500]
        # flag = adb_com.tap_center(rect)
        # print('tap_center , flag = ' + str(flag))

        # ###
        # flag = adb_com.touch_screen(300,300)
        # print('touch_screen , flag = ' + str(flag))

        # ###
        # from common_utility.general_util.rectangle import Point,RectAngle
        # sw = RectAngle(Point(100,100), Point(300,300))
        # duration = 400
        # flag = adb_com.swipe(sw.begin.x, sw.begin.y, sw.end.x, sw.end.y, duration)
        # print('swipe , flag = ' + str(flag))

        # ###
        # flag = adb_com.is_connect_android()
        # print('is_connect_android , flag = ' + str(flag))

        # ###
        # dev_list = adb_com.get_connect_adb_devices()
        # print('get_connect_adb_devices , dev_list = ' + str(dev_list))

        # ###
        # ret = adb_com.get_android_version()
        # print('get_android_version , ret = ' + str(ret))

        # ###
        # ret = adb_com.get_android_build_version()
        # print('get_android_build_version , ret = ' + str(ret))

        # ###
        # cmd = 'adb devices'
        # result = adb_com.adb_shell_with_show_result(cmd) # not recommended
        # ret_bool = adb_com.cnv_complete_process(result,'func_name',True,1)
        # print('cnv_complete_process , ret_bool = ' + str(ret_bool))
        # ret_str = adb_com.cnv_complete_process(result,'func_name',True,2)
        # print('cnv_complete_process , ret_str = ' + str(ret_str))

        # ###
        # package_name = 'com.android.chrome'
        # ret = adb_com.get_package_version(package_name)
        # print('get_package_version , ret = ' + str(ret))

        # ###
        # ret = adb_com.get_device_product_model()
        # print('get_device_product_model , ret = ' + str(ret))

        # ###
        # ret = adb_com.get_emei()
        # print('get_emei , ret = ' + str(ret))

        # ###
        # ret = adb_com.get_phone_number()
        # print('get_phone_number , ret = ' + str(ret))

        # ###
        # is_logout = False
        # nums = [13,14,17,18]
        # for num in nums:
        #     ret = adb_com.get_servece_call_iphonesubinfo(num,is_logout)
        #     print('get_servece_call_iphonesubinfo {} , ret = {}'.format(num,ret))

        # ###
        # package_name = 'com.android.chrome'
        # activity = ' .MainActivity'
        # activity = '/ .Main'
        # ret = adb_com.start_package(package_name,activity)
        # print('start_package , ret = ' + str(ret))

        # ###
        # package_name = 'chrome'
        # package_name = 'com.'
        # package_name = 'com.google'
        # ret = adb_com.get_info_package_list(package_name)
        # print('get_info_package_list , ret = ' + str(ret))

        # ###
        # package_name = 'com.android.chrome'
        # ret = adb_com.stop_package(package_name)
        # print('stop_package , ret = ' + str(ret))

        # ###
        # package_name = 'com.android.chrome'
        # activity = ' .MainActivity'
        # ret = adb_com.reboot_package(package_name,activity)
        # print('reboot_package , ret = ' + str(ret))

        # ###
        from common_utility.adb_util.adb_key_const import ConstKeycode
        keycode = ConstKeycode.HOME
        ret = adb_com.input_keyevent(keycode)
        print('input_keyevent , ret = ' + str(ret))

        return
    except:
        traceback.print_exc()


if __name__ == '__main__':
    test_adb_com()