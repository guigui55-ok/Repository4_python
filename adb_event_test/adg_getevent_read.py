from os import write
import import_init
import log_init
from log_init import initialize_logger
import binascii

import common_util.file_util.file_general as file_general
import common_util.adb_util.adb_common as adb_common

class AdbEvent():
    e_type:str = ''
    e_code:str = ''
    e_value:str = ''
    def __init__(self,e_type,e_code,e_value) -> None:
        self.e_type = e_type
        self.e_code = e_code
        self.e_value = e_value

    def print_data(self,num=-1):
        value = (self.e_type,self.e_code,self.e_value)
        n_str = ''
        if num != -1 : n_str = str(num) + ':'
        print(n_str + value)
    def encoding_utf8(self,value:str):
        buf = value.replace('0x','')
        return bytes(buf,encoding='utf-8',errors='replace')

    def encoding_utf8_align_digit(self,value:str,digit:int):
        buf = self.encoding_utf8(value)
        if len(buf) < digit:
            times = digit - len(buf)
            for i in range(times):
                buf = b'\00' + buf
            return buf
        elif len(buf) == digit:
            return buf
        else:
            assert 'AdbEvent.encoding_utf8_align_digit : len(buf) > digit'
    def get_byte_type(self):
        return self.encoding_utf8_align_digit(self.e_type,4)
    def get_byte_code(self):
        return self.encoding_utf8_align_digit(self.e_code,4)
    def get_byte_value(self):
        return self.encoding_utf8_align_digit(self.e_value,8)

import traceback

def write_byetes(data:bytes,file_name):
    f = open(file_name, 'ab')
    f.write(data)
    f.close()

class AdbEventWriter():
    file_path = ''
    def __init__(self,file_path) -> None:
        self.file_path = file_path

    def write_interval(self,val=None):
        if val == None:
            data = b''
            for i in range(8):
                data += b'\x00'
        self.write_byetes(data)

    def write_byetes(self,data:bytes,file_path=None):
        if file_path == None: file_path = self.file_path
        f = open(file_path, 'ab')
        f.write(data)
        f.close()
    
    def write_adb_event_data(self,data:AdbEvent):
        self.write_interval()
        self.write_byetes(data.get_byte_type())
        self.write_byetes(data.get_byte_code())
        self.write_byetes(data.get_byte_value())

    # def write_event_type(self,data:bytes):
    #     """2byte"""
    #     buf = data.replace('0x','')

    # def write_event_code(self):
    #     """2byte"""
    #     pass
    # def write_event_value(self):
    #     """4byte"""
    #     pass

def read_event_file():
    try:
        # set log object
        logger = initialize_logger()
        # set path
        import pathlib,os
        dir = str(pathlib.Path(__file__).parent)
        file_name = 'getevent.txt'
        file_path = os.path.join(dir,file_name)
        # read file
        read_lines = file_general.read_line_file(logger,file_path)
        print('len(read_lines) = ' + str(len(read_lines)))
        #
        adb_events = []
        for line in read_lines:
            print(line[:-1])
            e_type,e_code,e_value = cnv_adb_event_str_to_hex(line[:-1])
            # print(e_type,e_code,e_value)
            e = AdbEvent(e_type,e_code,e_value)
            adb_events.append(e)
        
        bin_name = 'sendevent.bin'
        bin_file_path =  os.path.join(dir,bin_name)

        os.remove(bin_file_path)

        writer = AdbEventWriter(bin_file_path)
        data:AdbEvent
        i = 0
        for data in adb_events:
            i+=1
            data.print_data(i)
            writer.write_adb_event_data(data)
        # import common_util.adb_util.adb_common as adb_common
        # ev :AdbEvent
        # before = 'adb shell print '
        # after = ' ^> /dev/input/event2'
        # cmd = ''
        # for ev in adb_events:
        #     cmd = ''
        #     cmd = '"\\' + ev.e_type 
        #     cmd += '\\' + ev.e_code 
        #     cmd += '\\' + ev.e_value
        #     cmd += '"'
        #     cmd = before + cmd + after
        #     adb_common.excute_command(logger,cmd)
        android_path = '/sdcard/'
        flag = adb_common.push(logger,bin_file_path,android_path)
        cmd = 'adb shell "cat /sdcard/event.bin > /dev/input/event2"'
        flag = adb_common.excute_command(logger,cmd)
        return
    except:
        traceback.print_exc()

def cnv_adb_event_str_to_hex(value:str):
    """0001 014a 00000001"""        
    try:
        ret:hex = 0
        values = value.split(' ')
        if len(values)<3: return hex(0),hex(0),hex(0)
        e_type:int = cnv_hex_str_to_int(values[0])
        e_code:int = cnv_hex_str_to_int(values[1])
        e_value:int = cnv_hex_str_to_int(values[2])
        return hex(e_type),hex(e_code),hex(e_value)
    except:
        traceback.print_exc()
        return hex(0),hex(0),hex(0)

def cnv_hex_str_to_int(value:str):
    """
    0001
    014a
    00000001
    """
    try:
        hex_str = ''
        for c in value:
            if c != '0':
                hex_str += c
        ret:int = 0
        for i in range(len(hex_str)):
            n = len(hex_str)-i-1
            c = hex_str[n:n+1]
            ret += calc_str_to_hex(c,i)
        return ret
    except:
        traceback.print_exc()
        return 0

def calc_str_to_hex(char:str,digit)->int:
    try:
        import re
        if re.match('[0-9]',char): n = int(char)
        elif re.match('[aA]',char): n = 10
        elif re.match('[bB]',char): n = 11
        elif re.match('[cC]',char): n = 12
        elif re.match('[dD]',char): n = 13
        elif re.match('[eE]',char): n = 14
        elif re.match('[fF]',char): n = 15
        else: n = 0
        n = n * pow(16,digit)
        return n
    except:
        traceback.print_exc()
        return hex(0)

def isnumeric(value:str):
    try:
        n = int(value)
        return True
    except:
        return False


def main():
    read_event_file()

main()