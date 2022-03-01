
import sys,pathlib,os

def sys_path_appen(path):
    sys.path.append(path)
    print('    sys.path.append = ' + path)

try:
    # common root
    path = r'C:\Users\OK\source\repos\Repository4_python\common_utilty'
    sys_path_appen(path)
    # test common
    path = str(pathlib.Path(__file__).parent)
    sys_path_appen(path)
except:
    import traceback
    traceback.print_exc()
print('### ' + __file__)