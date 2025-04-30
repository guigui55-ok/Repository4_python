
import os,pathlib

INPUT_FILE_NAME = 'input.txt'
INPUT_TEMP_FILE_NAME = 'input_temp.txt'

DIR_PATH = os.path.dirname( __file__)
TEST_DATA_DIR_NAME = 'test_data'
INPUT_DIR = os.path.join(DIR_PATH,TEST_DATA_DIR_NAME)

def input_init_new(test_name:str,test_num:int=1):
    file_name = test_name + '.txt'
    read_path = os.path.join(INPUT_DIR,file_name)
    begin_marker = '######### {} #########\n'.format(test_num)
    end_marker = '========== answer ==========\n'
    is_read = False
    read_data = []
    
    f = open(read_path,'r',encoding='utf-8')
    count = 0
    while True:
        count += 1
        if count > 500:
            break
        line = f.readline()
        if is_read:
            if line == end_marker:
                is_read = False
                break
            read_data.append(line)
        if line == begin_marker:
            is_read = True
            f.readline()
    f.close()
    read_data.append('\n')

    write_path = os.path.join(DIR_PATH, INPUT_TEMP_FILE_NAME)
    with open(write_path,'w',encoding='utf-8')as f:
        f.writelines(read_data)

def input_init(file_num:int=0):
    import shutil,os
    if file_num>0:
        input_file_name = os.path.splitext(INPUT_FILE_NAME)[0]+ str(file_num) + '.txt'        
    else:
        input_file_name = INPUT_FILE_NAME

    src_path = os.path.join(DIR_PATH, input_file_name)
    dist_path = os.path.join(DIR_PATH, INPUT_TEMP_FILE_NAME)
    shutil.copy(src_path,dist_path)
    if True:
        # debug_print_file(dist_path)
        pass

def debug_print_file(path:str):
    with open(path, 'r',encoding='utf-8')as f:
        buf = f.read()
    print('---------- inputinit')
    print(buf)
    print('----------')

def input():
    path = os.path.join(DIR_PATH, INPUT_TEMP_FILE_NAME)
    with open(path, 'r', encoding='utf-8')as f:
        buf = f.read()
    lines = buf.split('\n')
    ret = lines[0]
    if ret == '':
        raise Exception('EOFError: EOF when reading a line')
    #
    wbuf = ''
    for buf in lines[1:]:
        wbuf += buf + '\n'
    wbuf = wbuf[:-1]
    with open(path, 'w', encoding='utf-8')as f:
        f.write(wbuf)
    # print(ret)
    return ret
    