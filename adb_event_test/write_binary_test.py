
from os import read
import traceback

def get_dir_path(file_name=''):
    import pathlib,os
    read_path = str(pathlib.Path(__file__).parent)
    if file_name !='':
        read_path = os.path.join(str(pathlib.Path(__file__).parent),file_name)
    return read_path

def print_list(int_list_list:list):
    buf = ''
    sep = ' - '
    for list in int_list_list:
        buf += str(list) + sep
    buf = buf[:-len(sep)]
    print(buf)

def print_int_list(int_list,block=8,new_line_pass_block_cnt=2):
    try:
        index_count = 0
        block_count = 0
        buf = []
        write_buf = []
        for val in int_list:
            buf.append(val)
            if index_count >= (block-1):
                index_count = 0
                write_buf.append(buf)
                buf = []
                block_count += 1
            else:
                index_count += 1
            if block_count >= new_line_pass_block_cnt:
                block_count = 0
                print_list(write_buf)
                write_buf = []
                # buf = []
            
    except:
        traceback.print_exc()


def hex_str_to_bytes(value:str):
    buf = value.replace('0x','')
    return bytes(buf,encoding='utf-8',errors='replace')

def int_to_bytes(value:int):
    return hex_str_to_bytes(str(value))

def write_byetes(data:bytes,file_name):
    f = open(file_name, 'ab')
    f.write(data)
    f.close()

def read_binary_lines(file_path:str):
    f = open(file_path, 'rb')
    lines = f.readlines()
    f.close()
    return lines

def read_binary_all(file_path:str):
    f = open(file_path, 'rb')
    data = f.read()
    f.close()
    return data

def read_binary(file_path:str):
    f = open(file_path, 'rb')
    data = f.read1()
    f.close()
    return data

def read_test(file_path=''):
    try:
        file_name = 'event_copy.bin'
        read_path = get_dir_path(file_name)
        if file_path != '':
            read_path = file_path
        ############
        # read line
        # lines = read_binary_lines(read_path)
        # for i in range(len(lines)):
        #     line = lines[i]
        #     print(line)

        ############
        # read all
        data = read_binary_all(read_path)
        # print(data)

        ############
        # read all
        read_data = read_binary_all(read_path)
        # print(read_data)
        list = []
        for d in read_data:
            list.append(int(d))
        print_int_list(list)
        return data
    except:
        traceback.print_exc()

def test_read_write():
    try:
        # read
        file_name = 'event_copy.bin'
        read_path = get_dir_path(file_name)
        data = read_test(read_path)
        # cnv bytes -> int

        # cnv int -> bytes

        # put list together 一つにつなげる
        # write
        file_name = 'event_copy2.bin'
        write_path = get_dir_path(file_name)
        write_byetes(data, write_path)
        # read
        read_test(write_path)
        return
    except:
        traceback.print_exc()

def write_test():
    try:
        file_name = 'test.bin'
        write_path = get_dir_path(file_name)
        # value = 3
        # data = int_to_bytes(value)
        # value = '\x00:'
        # data = hex_str_to_bytes(value)
        data:bytes = b'\x00:'
        data:bytes = b'\x00:'
        write_byetes(data, write_path)
        ############
        # read all
        read_data = read_binary_all(write_path)
        # print(read_data)
        list = []
        for d in read_data:
            list.append(int(d))
        print_int_list(list)
        return
    except:
        traceback.print_exc()

# read_test()
# write_test()
test_read_write()