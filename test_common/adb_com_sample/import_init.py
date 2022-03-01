
import sys,pathlib,os

def sys_path_appen(path):
    sys.path.append(path)
    print('    sys.path.append = ' + path)

print('### ' + __file__)
try:
    # common root
    path = r'C:\Users\OK\source\repos\Repository4_python'
    sys_path_appen(path)
    # test common
    path = str(pathlib.Path(__file__).parent.parent)
    sys_path_appen(path)
except:
    import traceback
    traceback.print_exc()

