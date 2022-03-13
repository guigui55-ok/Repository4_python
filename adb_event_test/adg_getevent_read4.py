
import traceback

import import_init
import log_init
from log_init import initialize_logger

import common_util.file_util.file_general as file_general
import common_util.adb_util.adb_common as adb_common


from adb_getevent_io import AdbEventWriter,AdbEvent,cnv_adb_event_str_to_hex


#[ 1275520.969769] EV_ABS       ABS_MT_POSITION_X    00000155

class AdbEventValues():
    """
    #[ 1275520.969769] EV_ABS       ABS_MT_POSITION_X    00000155(1)
    から、読み取った
    #TIME1,TIME2,EVENT,TYPE,VALUE(2)
    をstr、から hex に変換する
    (2)を扱うクラス
    """
    event_str:str=''
    type_str:str=''
    value_str:str=''
    time1:int=0
    time2:int=0
    event_hex:str=''
    type_hex:str=''
    value_hex:str=''
    def __init__(self,values:'list[str]'=None) -> None:
        if values == None:return
        if len(values)<5:
            print('len(values)<5 , values='+str(values))
            return
        self.time1 = int(values[0])
        self.time2 = int(values[1])
        self.event_str = values[2]
        self.type_str = values[3]
        self.value_str = values[4]
    def get_values_hex(self):
        """0003 0035 0000013e の形式で値を取得する"""
        ret = self.event_hex + ' ' + self.type_hex + ' ' + self.value_hex
        return ret
    def is_nothing(self):
        """値があるか判定する"""
        if self.event_str == '' or \
            self.type_str == '' or \
            self.value_str == '':
            return True
        else:
            return False

class AdbEventLine():
    """
    [ 1275520.969769] EV_ABS       ABS_MT_POSITION_X    00000155(1)
    から、読み取った
    TIME1,TIME2,EVENT,TYPE,VALUE(2)
    をstr、から hex に変換する
    (1)を扱うクラス
     time1、time2はintのまま
    """
    def __init__(self,tl_value:str='',base_time2:int=0) -> None:
        self.tl_value:str = tl_value
        self.values_split = self.set_value(tl_value)
        self.adb_values = AdbEventValues(self.values_split)
    def set_value(self,tl_value:str):
        """記号などをすべてスペースに変換して、splitした、値を分割、メンバへ格納する"""
        value = tl_value
        value = self.remove_double_space(value)
        value = value.replace('[',' ')
        value = value.replace(']',' ')
        value = value.replace('.',' ')
        values = value.split(' ')
        while True:
            if '' in values:
                values.remove('')
            else:
                break
        return values
    def remove_double_space(self,value:str)->str:
        """2つ以上連増するスペースをなくする"""
        while True:
            if value.find('  ')>=0:
                value = value.replace('  ',' ')
            else:
                return value
        return value
    def cnv_adb_event_name_to_hex_str(self):
        #TIME1,TIME2,EVENT,TYPE,VALUE
        #この順番にデータが入っている
        values = self.values_split
        if len(values):
            self.adb_values = AdbEventValues(values)




import json_util.json_class as json
class AdbEventLineAnalyser():
    """"adb shell getevent -tlコマンドで取得できる文字列を、-tlではないものに変換するクラス
    EV_SYN":"0",など(EVENT_NAMEを16進にする値)を記録した、変換するためのjsonファイルを読み込んでおくこと"""
    def __init__(self,json_path:str) -> None:
        self.json_path:str = json_path
        self.value_dict:dict = self.get_value_from_json()
    def get_value_from_json(self):
        import os
        if not os.path.exists(self.json_path): raise Exception('path not exists, path='+self.json_path)
        js = json.JsonUtil(self.json_path)
        return js.values
    def cnv_adb_event_name_to_dec_str(self,adb_values:AdbEventValues)->AdbEventValues:
        """event、type、valueを文字列から数字（16進）に変換する（jsonファイルの値に置き換え）
"ABS_MT_TRACKING_ID":"39",
"SYN_REPORT":"0",
"EV_KEY":"1",

        """
        adb_values.event_hex = self.get_value_from_json_dict(adb_values.event_str)
        adb_values.type_hex = self.get_value_from_json_dict(adb_values.type_str)
        adb_values.value_hex = self.get_value_from_json_dict(adb_values.value_str)
        return adb_values

    def get_value_from_json_dict(self,value:str):
        jd = self.value_dict
        hex_str = value
        if value in jd.keys():
            hex_str = jd[value]
        return hex_str



def sendevents(logger,event_lines:list,dir_path,bin_name:str='event.bin'):
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
    # bin_name = 'event.bin'
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


def sendevents2(logger,tl_analyzer:AdbEventLineAnalyser,event_lines:list,dir_path,bin_name:str='event.bin'):
    # 読み込んだリストから、type,code,valueを読み込む
    import os
    adb_events = []
    count = 0
    now_time2=0
    for line in event_lines:
        # print(line[:-1])
        adb_line_val = AdbEventLine(line[:-1])
        adb_event_values = adb_line_val.adb_values
        adb_event_values = tl_analyzer.cnv_adb_event_name_to_dec_str(adb_event_values)
        line_cnv = adb_event_values.get_values_hex()
        # if adb_event_values.event_hex == '0':

        if not adb_event_values.is_nothing():
            print(line_cnv)
            e_type,e_code,e_value = cnv_adb_event_str_to_hex(line_cnv)
            # print(e_type,e_code,e_value)
            e = AdbEvent(e_type,e_code,e_value,adb_event_values.time2)
            adb_events.append(e)
        count+=1
    # ファイル名、パスをセットする
    # bin_name = 'event.bin'
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


def read_to_ffffff_or_eof(lines:'list[str]',start=0):
    """
    以下のイベントを ffffffffまで塊で読み込む
0003 0039 000002ea
0003 003a 00000071
    """
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



def read_event_file2():
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



def read_event_file3():
    try:
        # set log object
        logger = initialize_logger()
        # set path
        import pathlib,os
        dir_path = str(pathlib.Path(__file__).parent)
        dir_path = ''
        file_name = 'getevent_tl_2.txt'
        file_name = 'getevent_tl_1.txt'
        file_path = os.path.join(dir_path,file_name)
        # read file
        read_lines = file_general.read_line_file(logger,file_path)
        print('len(read_lines) = ' + str(len(read_lines)))
        #
        import time
        pos = 0
        json_path = './adb_event_hex.json'
        tl_analyzer = AdbEventLineAnalyser(json_path)
        while(pos<len(read_lines)):
            # time.sleep(1)
            pos,lines = read_to_ffffff_or_eof(read_lines,pos)
            sendevents2(logger,tl_analyzer, lines,dir_path)
            pos = pos + 1
        
        return
    except:
        traceback.print_exc()


def main():
    read_event_file3()

main()