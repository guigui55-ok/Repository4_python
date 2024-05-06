


import zipfile
import shutil
from pathlib import Path

def get_file_name():
    dir_path = Path(__file__).parent
    file_name = '__test_read_file_name.txt'
    file_path = str(dir_path.joinpath(file_name))
    encoding = 'shift-jis'
    encoding = 'cp932'
    encoding = 'utf-8'
    with open (file_path, 'r', encoding=encoding)as f:
        buf = f.read()
    buf = buf.strip()
    return buf


def test_main():
    pass
    # https://note.nkmk.me/python-zipfile/
    dir_path = Path('C:\ZMyFolder\_job\_ost')
    file_name = get_file_name()
    file_path = dir_path.joinpath(file_name)
    print('file_path = {}'.format(file_path))
    with zipfile.ZipFile(str(file_path)) as zf:
        # zf.extract('file.txt', 'dir_out_extract')
        # zf.extract('dir_sub/file_sub.txt', 'dir_out_extract')
        zf.extractall('__temp/')
        zip_path = zf.filename
    
    print('unzip_file_path = {}'.format(zip_path))



if __name__ == '__main__':
    print()
    print('*****')
    test_main()

