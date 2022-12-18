


import os
import pathlib
def main():
    print()
    print('*****')
    ###
    read_dir_path_str = r'C:\Users\OK\source\repos\test_media_files\_js_test\local_save'
    read_file_name = 'index.html'
    write_dir_path = pathlib.Path(__file__).parent
    write_file_name = read_file_name
    write_path_str = str(write_dir_path.joinpath(write_file_name))
    ###
    path_str = os.path.join(read_dir_path_str,read_file_name)
    with open(path_str ,'r', encoding='utf-8')as f:
        data = f.read()
    ret = data
    ret = ret.replace('＜','<')
    ret = ret.replace('＞','>')
    with open(write_path_str, 'w', encoding='utf-8')as f:
        f.write(ret)
    print('write_path = {}'.format(write_path_str))
    return


if __name__ == '__main__':
    main()