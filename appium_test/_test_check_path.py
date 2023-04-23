


import os
import pathlib
def main():
    name = r'c:\Users\OK\source\repos\Repository4_python\appium_test\log\logger_test.log'
    # Case A
    flag = False
    if not pathlib.Path(name).exists():
        if not pathlib.Path(name).is_dir():
            path = str(pathlib.Path(name).parent)
            os.mkdir(path)
            flag = True
    # Case B
    flag = False
    if pathlib.Path(name).is_file():
        path = str(pathlib.Path(name).parent)
        if not pathlib.Path(name).parent.exists():
            os.mkdir(str(pathlib.Path(name).parent))

if __name__ == '__main__':
    main()