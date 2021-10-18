import os

file_name = 'test.txt'
directory = os.getcwd()
path = directory + '\\' + file_name

if (os.isfile(path)):
    print('file path is not found')

else:
    pass

