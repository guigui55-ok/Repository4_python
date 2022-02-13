


from numpy import true_divide


def get_dir_path():
    import pathlib
    dir_path = str(pathlib.Path(__file__).parent.joinpath('test_data'))
    return dir_path

def create_data_all():
    dir_path = get_dir_path()
    base_file_name = 'test.json'
    for i in range(5):
        file_name = base_file_name.replace('.',str(i)+'.')
        create_data(dir_path,file_name,i)

def create_data(dir_path,file_name,num:int):
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

def get_file_list():
    dir_path = get_dir_path()
    import os
    all_list = os.listdir(dir_path)
    return all_list

def pathjoin(dir_path,file_name):
    import os
    return os.path.join(dir_path,file_name)

def read_value():
    dir_path = get_dir_path()
    file_name = 'test_1.txt'
    path = pathjoin(dir_path,file_name)
    # read
    with open(path,'r')as f:
        buf = f.readlines()
    return buf


def sepalate_value(lines:list[str],sepalete_list:list[str]):
    blocks:list[list[str]] = []
    block:list[str] = []
    for i in range(len(lines)):
        line = lines[i]
        if is_match_in_list(line,sepalete_list):
            blocks.append(block)
            block = []
        else:
            pass
        block.append(line)

def is_match_in_list(line:str,sepalete_list:list[str]):
    for i in range(len(sepalete_list)):
        chk = sepalete_list[i]
        if line == chk:
            return True
    return False

def update_json_main(blocks:list[list[str]]):
    for i in range(1,len(blocks)):
        

if __name__ == '__main__':
    # create_data_all()
    # make_list()