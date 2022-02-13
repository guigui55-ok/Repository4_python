

def get_path()->str:
    import pathlib,os
    file_name = 'test.csv'
    sub_dir = 'test_data'
    path = os.path.join(pathlib.Path(__file__).parent,sub_dir,file_name)
    return path

def get_path_(base_path:str,file_name:str='',sub_dir:str=''):
    import pathlib,os
    file_name = 'test.csv'
    sub_dir = 'test_data'
    if sub_dir != '':
        path = os.path.join(pathlib.Path(base_path).parent,sub_dir,file_name)
    else:
        path = os.path.join(pathlib.Path(base_path).parent,file_name)
    return path