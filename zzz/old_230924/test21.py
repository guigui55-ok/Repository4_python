

import pathlib
path = str(pathlib.Path(__file__).parent.joinpath('test1.py'))
encoding= 'UTF-8'
encoding= 'utf-8'
with open(path, 'r', encoding=encoding)as f:
    buf = f.read()

print('*****')
print(len(buf))