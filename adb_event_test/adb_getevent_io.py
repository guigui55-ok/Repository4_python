import binascii
import traceback

class AdbSendEventDuration():
    time_lows:list
    time_highs:list
    base_time_high:int
    base_time_low:int
    interval:int
    now_time_high:int
    now_time_low:int
    def __init__(self,interval=110000) -> None:
        self.interval = interval
        self.base_time_high = self.set_time_now()
        self.base_time_low = 0
        self.now_time_high = self.base_time_high
        self.now_time_low = 0
    def set_time_now(self):
        import datetime
        dt_now = datetime.datetime.now()
        h = dt_now.hour
        m = dt_now.minute
        s = dt_now.second
        h_s = 60*60*h
        m_s = 60*h
        self.base_time_high = h_s + m_s + s
        return self.base_time_high
    def add_interval(self):
        self.now_time_low += self.interval



class AdbEvent():
    """
    adb shell getevent で取得されたデータを取得する際のユーティリティ
    """
    e_time_low:str = ''
    e_time_high:str = ''
    e_type:str = ''
    e_code:str = ''
    e_value:str = ''
    def __init__(self,e_type,e_code,e_value,e_time_high=0,e_time_low=0) -> None:
        self.e_type = str(e_type)
        self.e_code = str(e_code)
        self.e_value = str(e_value)
        self.e_time_high = str(e_time_high)
        self.e_time_low = str(e_time_low)

    def print_data(self,num=-1):
        """
        メンバ変数を Terminal に出力する
        """
        value = [self.e_time_high, self.e_time_low, self.e_type,self.e_code,self.e_value]
        n_str = ''
        # for 文などで index も表示させたいときは num を指定する
        if num != -1 : n_str = str(num) + ':'
        print(n_str + str(value))
            
    def get_value_as_str(self,value:str):
        """
        str 型のhexデータを取得する
        ex)
        '0x123' => 123
        'a0' => a0
        """
        if value.find('0x') < 0:
            return value
        if value[:2] == '0x':
            value = value[2:]
        return value
    
    def get_little_endian_from_int(self,val_int:int,size):
        val_bytes = val_int.to_bytes(size, byteorder="little")
        return val_bytes

    def get_little_endian(self,hex_str:str,size):        
        val_str = self.get_value_as_str(hex_str)
        val_int:int = int(val_str,16)
        val_bytes = val_int.to_bytes(size, byteorder="little")
        return val_bytes

    def get_byte_type(self):
        return self.get_little_endian(self.e_type,2)
    def get_byte_code(self):
        return self.get_little_endian(self.e_code,2)
    def get_byte_value(self):
        return self.get_little_endian(self.e_value,4)
    def get_byte_time_low(self):
        return self.get_little_endian(self.e_time_low,8)
    def get_byte_time_high(self):
        return self.get_little_endian(self.e_time_high,8)
    


class AdbEventWriter():
    """    
    adb shell getevent で取得されたデータをファイルへ書き込む際のユーティリティ
    """
    file_path = ''
    def __init__(self,file_path) -> None:
        self.file_path = file_path

    def write_interval(self,val=None):
        if val == None:
            data = b''
            for i in range(4):
                data += b'\x00'
        self.write_byetes(data)
    
    def write_byetes(self,data:bytes,file_path=None):
        if file_path == None: file_path = self.file_path
        f = open(file_path, 'ab')
        f.write(data)
        f.close()
    
    def write_adb_event_data(self,data:AdbEvent):
        time_high = data.get_byte_time_high()
        time_low = data.get_byte_time_low()
        b_type = data.get_byte_type()
        b_code = data.get_byte_code()
        b_value = data.get_byte_value()
        self.write_byetes(time_high)
        self.write_byetes(time_low)
        self.write_byetes(b_type)
        self.write_byetes(b_code)
        self.write_byetes(b_value)

def isnumeric(value:str):
    try:
        n = int(value)
        return True
    except:
        return False

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


def cnv_adb_event_str_to_hex(value:str):
    """
    adb shell getevent で取得された以下データを str 型(16進数) で読み込む
    戻り値：
        str,str,str
    value :ex)
    '0001 014a 00000001'

    """
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