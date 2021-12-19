
import traceback

import import_init
from log_init import initialize_logger
from adb_getevent_util import adb_sendevents

def adb_send_event_sample():
    try:
        # set log object
        logger = initialize_logger()
        
        from common_util.adb_util.adb_common import get_connect_adb_devices
        ret = get_connect_adb_devices(logger)
        # set path
        import pathlib,os
        dir_path = str(pathlib.Path(__file__).parent)
        file_name = 'getevent.txt'
        file_name = 'getevent_2.txt'
        file_name = 'getevent_9.txt'
        # set value
        pc_read_getevent_dir = dir_path
        pc_read_getevent_file_name = file_name
        pc_binary_dir_path = dir_path
        binary_file_name = 'event.bin'
        android_sd_dir_path = '/sdcard'
        dev_input_event = '/dev/input/event2'
        interval_sec = 2
        control_interval_sec = 0.22
        adb_sendevents(
            logger,
            pc_read_getevent_dir,
            pc_read_getevent_file_name,
            pc_binary_dir_path,
            binary_file_name,
            android_sd_dir_path,
            dev_input_event,
            interval_sec,
            control_interval_sec)
        return True
    except:
        traceback.print_exc()
        return False



def main():
    adb_send_event_sample()

main()