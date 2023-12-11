
import pathlib
file_name = 'test.py'
file_name = 'test2.py'
path = pathlib.Path(__file__).joinpath(file_name)

# buf = open(file_name, encoding='cp932').readline()
buf = open(file_name, encoding='utf-8').readline()
print(buf)