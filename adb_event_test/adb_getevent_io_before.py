import binascii
import traceback

class AdbEvent():
    e_time_low:str = ''
    e_time_high:str = ''
    e_type:str = ''
    e_code:str = ''
    e_value:str = ''
    time_low_int:list
    time_high_int:list
    type_int:list
    code_int:list
    value_int:list
    def __init__(self,e_type,e_code,e_value,e_time:int) -> None:
        self.e_type = e_type
        self.e_code = e_code
        self.e_value = e_value
        # self.set_e_time_low(e_time)
        # self.set_e_time_high(0)
        self.e_time_low = str(e_time)
        self.e_time_high = '0'

    def set_e_time_high(self,time:int=0):
        self.e_time_high = hex(0)
    def set_e_time_low(self,time:int):
        self.e_time_low = hex(time*10)

    def print_data(self,num=-1):
        value = (self.e_type,self.e_code,self.e_value)
        n_str = ''
        if num != -1 : n_str = str(num) + ':'
        print(n_str + str(value))
    def encoding_utf8(self,value:str):
        buf = value.replace('0x','')
        return bytes(buf,encoding='utf-8',errors='replace')


    def str_to_int_list(self,value,digit):
        if (len(value) + digit) % 2 == 1:
            assert 'AdbEvent.str_to_int_list (len(value) + digit) % 2 == 1 , return'
        ret_list = []
        value = self.str_align_digit(value,digit)
        for i in range(0,len(value),2):
            buf = value[i] + value[i+1]
            buf_int = int(buf)
            ret_list.append(buf_int)
        return ret_list

    def str_align_digit(self,value,digit):
        if len(value) < digit:
            times = digit - len(value)
            for i in range(times):
                value = '0' + value
        elif len(value) == digit:
            return value
        else:
            assert 'AdbEvent.str_align_digit : len(value) > digit'
            

    def encoding_utf8_align_digit(self,value:str,digit:int) ->bytes:
        buf:bytes = self.encoding_utf8(value)
        if len(buf) < digit:
            times = digit - len(buf)
            for i in range(times):
                buf = b'\00' + buf
            return buf
        elif len(buf) == digit:
            return buf
        else:
            assert 'AdbEvent.encoding_utf8_align_digit : len(buf) > digit'

    def get_value_as_int(self,value:str):
        if value[:2] == '0x':
            value = value[2:]
        return value

    def get_byte_type(self):
        val_str = self.get_value_as_int(self.e_type)
        val_int:int = int(val_str,16)
        val = val_int.to_bytes(2, byteorder="little")
        return val
        # return self.encoding_utf8_align_digit(self.e_type,4)
    def get_byte_code(self):
        val_str = self.get_value_as_int(self.e_code)
        val_int:int = int(val_str,16)
        val = val_int.to_bytes(2, byteorder="little")
        return val
        # return self.encoding_utf8_align_digit(self.e_code,4)
    def get_byte_value(self):
        val_str = self.get_value_as_int(self.e_value)
        val_int:int = int(val_str,16)
        val = val_int.to_bytes(4, byteorder="little")
        return val
        # return self.encoding_utf8_align_digit(self.e_value,8)
    def get_byte_time_low(self):
        val_str = self.get_value_as_int(self.e_time_low)
        val_int:int = int(val_str,16)
        val = val_int.to_bytes(8, byteorder="little")
        return val
        # return self.encoding_utf8_align_digit(self.e_time_low,8)
    def get_byte_time_high(self):
        val_str = self.get_value_as_int(self.e_time_high)
        val_int:int = int(val_str,16)
        val = val_int.to_bytes(8, byteorder="little")
        return val
        # return self.encoding_utf8_align_digit(self.e_time_high,8)
    
    def get_little_endian(self,hex_str:str):
        bytes_be = bytes.fromhex(hex_str)
        return self.get_little_endian_from_bytes(bytes_be)

    def get_little_endian_from_bytes(self,bytes_be:bytes):
        bytes_le = bytes_be[::-1]
        return bytes_le

    def get_little_endian_as_str(self,bytes_le:bytes):
        return bytes_le.hex()
        
    def get_byte_little_endian_type(self):
        bytes_val = self.encoding_utf8_align_digit(self.e_type,4)
        le = self.get_little_endian_from_bytes(bytes_val)
        return le
    def get_byte_little_endian_code(self):
        bytes_val = self.encoding_utf8_align_digit(self.e_code,4)
        le = self.get_little_endian_from_bytes(bytes_val)
        return le
    def get_byte_little_endian_value(self):
        bytes_val = self.encoding_utf8_align_digit(self.e_value,8)
        le = self.get_little_endian_from_bytes(bytes_val)
        return le
    def get_byte_little_endian_time_high(self):
        bytes_val = self.encoding_utf8_align_digit(self.e_time_high,8)
        le = self.get_little_endian_from_bytes(bytes_val)
        return le
    def get_byte_little_endian_time_low(self):
        bytes_val = self.encoding_utf8_align_digit(self.e_time_low,8)
        le = self.get_little_endian_from_bytes(bytes_val)
        return le


class AdbEventWriter():
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
        # self.write_interval()
        # time_high = data.get_byte_little_endian_time_high()
        # time_low = data.get_byte_little_endian_time_low()
        # b_type = data.get_byte_little_endian_type()
        # b_code = data.get_byte_little_endian_code()
        # b_value = data.get_byte_little_endian_value()
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
        # print(str(time_low),str(b_type),str(b_code),str(b_value))


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