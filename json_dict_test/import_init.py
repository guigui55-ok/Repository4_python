
import sys,pathlib,os

def sys_path_appen(path):
    sys.path.append(path)
    print('    sys.path.append = ' + path)

print('### ' + __file__)
try:
    # import common_utility (common root)
    path = r'C:\Users\OK\source\repos\Repository4_python\common_utilty'
    sys_path_appen(path)
    # test common
    target = 'json_dict_test'
    try:
        while True:
            path = str(pathlib.Path(__file__).parent)
            if os.path.basename(path) == target:
                sys_path_appen(path)
                break
            if os.path.basename(path) == path:
                break
    except:
        import traceback
        traceback.print_exc()
except:
    import traceback
    traceback.print_exc()

BAR = '###############################################################'

def get_path_from_current(file_path,file_name):
    import os,pathlib
    path = str(pathlib.Path(file_path).parent.joinpath(file_name))
    return path