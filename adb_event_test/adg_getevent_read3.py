
import traceback

import import_init
import log_init
from log_init import initialize_logger

import common_util.file_util.file_general as file_general
import common_util.adb_util.adb_common as adb_common


from adb_getevent_io_before import AdbEventWriter,AdbEvent,cnv_adb_event_str_to_hex

def sendevents(logger,event_lines:list,dir_path):
    # 読み込んだリストから、type,code,valueを読み込む
    import os
    adb_events = []
    count = 0
    for line in event_lines:
        print(line[:-1])
        e_type,e_code,e_value = cnv_adb_event_str_to_hex(line[:-1])
        # print(e_type,e_code,e_value)
        e = AdbEvent(e_type,e_code,e_value,count)
        adb_events.append(e)
        count+=1
    # ファイル名、パスをセットする
    bin_name = 'event.bin'
    bin_file_path =  os.path.join(dir_path,bin_name)
    # ファイルが存在していたら削除する
    if os.path.exists(bin_file_path):os.remove(bin_file_path)
    # bin ファイルに書き込み
    writer = AdbEventWriter(bin_file_path)
    data:AdbEvent
    i = 0
    for data in adb_events:
        i+=1
        # data.print_data(i)
        writer.write_adb_event_data(data)
    # sdcard へ bin ファイルをコピーして、さらにsdard から本体へコピーする（イベントを実行する）
    android_path = '/sdcard/event.bin'
    flag = adb_common.push(logger,bin_file_path,android_path)
    cmd = 'adb shell "cat /sdcard/event.bin > /dev/input/event2"'
    flag = adb_common.excute_command(logger,cmd)

def read_to_ffffff_or_eof(lines,start=0):
    i:int
    ret_list = []
    try:
        if start > (len(lines)-1):
            return start, ret_list
        to_last = 0
        for i in range(len(lines))[start:]:
            value:str = lines[i]
            if value.find('ffffffff') >= 0:
                ret_list.append(value)
                to_last = 3
            else:                
                ret_list.append(value)
                if to_last > 0:
                    to_last -= 1
                    if to_last == 1:
                        break
            # eof
            if i == (len(lines)-1):
                break
        return i, ret_list
    except:
        traceback.print_exc()
        return i, ret_list



def read_event_file():
    try:
        # set log object
        logger = initialize_logger()
        # set path
        import pathlib,os
        dir_path = str(pathlib.Path(__file__).parent)
        dir_path = ''
        file_name = 'getevent.txt'
        file_name = 'getevent_2.txt'
        file_name = 'getevent_3.txt'
        file_path = os.path.join(dir_path,file_name)
        # read file
        read_lines = file_general.read_line_file(logger,file_path)
        print('len(read_lines) = ' + str(len(read_lines)))
        #
        import time
        pos = 0
        while(pos<len(read_lines)):
            pos,lines = read_to_ffffff_or_eof(read_lines,pos)
            sendevents(logger,lines,dir_path)
            time.sleep(1)
            pos = pos + 1
        return
    except:
        traceback.print_exc()




def main():
    read_event_file()

main()