


from fileinput import filename
from numpy import true_divide


def get_dir_path():
    import pathlib
    dir_path = str(pathlib.Path(__file__).parent.joinpath('test_data'))
    return dir_path

def create_data_all():
    # create json data main
    dir_path = get_dir_path()
    base_file_name = 'test.json'
    for i in range(5):
        file_name = base_file_name.replace('.',str(i)+'.')
        create_data(dir_path,file_name,i)

def create_data(dir_path,file_name,num:int):
    # create json data
    try:
        str_num = str(num)
        buf_dict1 : dict ={
            'key' + str_num + '1': 'value1',
            'key' + str_num + '2': 'value2',
            'key' + str_num + '3': 'value3'
        }
        import os
        path = os.path.join(dir_path,file_name)
        from util.json_dict import JsonDict
        jd = JsonDict(path,True)
        jd.values = buf_dict1
        jd.write_json()
        return
    except:
        import traceback
        traceback.print_exc()

def make_list():
    # make file_name list
    dir_path = get_dir_path()
    file_name = 'test0_file_name_list.txt'
    # get file list
    import os 
    all_list = os.listdir(dir_path)
    # file_list = [f for f in all_list if os.path.isfile(os.path.join(dir_path, f))]
    # make data
    buf:str = ''
    delimita:str = '\n'
    for f in all_list:
        buf += str(f) + delimita
    # write
    wpath = os.path.join(dir_path,file_name)
    with open(wpath,'w') as f:
        f.write(buf)
#-------------------

def get_file_list():
    dir_path = get_dir_path()
    import os
    all_list = os.listdir(dir_path)
    return all_list

def pathjoin(dir_path,file_name):
    import os
    return os.path.join(dir_path,file_name)

#-------------------
def update_main():
    dir_path = get_dir_path()
    file_name = 'test0_1.txt'
    file_name = 'test0_2.txt'
    file_list = get_file_list()
    lines = read_value(dir_path, file_name)
    line_blocks = sepalate_value(lines,file_list)
    for i in range(1,len(line_blocks)):
        line_block = line_blocks[i]
        update_json_main(line_block,dir_path)

def read_value(dir_path:str, file_name:str)->list[str]:
    path = pathjoin(dir_path,file_name)
    # read
    buf:list[str] = []
    with open(path,'r')as f:
        buf = f.readlines()
    for i in range(len(buf)):
        buf[i] = buf[i].replace('\n','')
    return buf


def sepalate_value(lines:list[str],sepalete_list:list[str]):
    line_blocks:list[list[str]] = []
    line_block:list[str] = []
    for i in range(len(lines)):
        line = lines[i]
        if is_match_in_list(line,sepalete_list):
            line_blocks.append(line_block)
            line_block = []
        else:
            pass
        line_block.append(line)
    else:
        line_blocks.append(line_block)
    return line_blocks

def is_match_in_list(line:str,sepalete_list:list[str]):
    for i in range(len(sepalete_list)):
        chk = sepalete_list[i]
        line = line.replace('\n','')
        if line == chk:
            return True
    return False

def update_json_main(line_block:list[str],dir_path:str):
    file_name , value = blocks_to_str_and_filename(line_block)
    from util.json_checker import JsonValueChecker
    jvc = JsonValueChecker(value)
    if jvc.is_current_format_json_piece():
        jvc.value = '{' + jvc.value + '}'
    if jvc.is_current_format_json():
        # update
        update_json(dir_path,file_name,jvc.value)

def update_json(dir_path:str,file_name:str,value:str):
    from util.json_dict import JsonDict
    path = pathjoin(dir_path,file_name)
    jd = JsonDict(path)
    value_dict = jd.str_to_dict(value)
    jd.update_value(value_dict)
    jd.write_json()
    print('success')
    print(path)
    print(value)

def str_to_dict(value:str):
    from util.csv_dict import CsvDict
    cd = CsvDict()
    from util.dict_list import DictList
    dl = DictList()

def blocks_to_str_and_filename(line_block:list[str]):
    ret:str = ''
    cnt = 0
    for line in line_block:
        if cnt != 0:
            ret += line + '\n'
        else:
            cnt = 1
    return line_block[0] ,ret 

if __name__ == '__main__':
    # create_data_all()
    # make_list()
    update_main()