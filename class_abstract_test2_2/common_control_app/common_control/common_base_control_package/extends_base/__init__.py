
"""
    このpackageの上層に以下pakageを配置する。
    target_name_list =['base_package','common_general']
"""
is_excute = False
print(is_excute)
if not is_excute:
    is_excute = True
print('######################################################################')
print('* '+__file__)
import sys,os,pathlib
import traceback
try:
    #
    target_name_list =['base_package','common_general']
    path = str(pathlib.Path(__file__))
    add_path = str(pathlib.Path(__file__).parent)
    sys.path.append(add_path)
    print('* sys.path.append = '+add_path)
    while True:
        path = str(pathlib.Path(path).parent)
        dir_name_list = os.listdir(path)
        for dir_name in dir_name_list:
            for target_name in target_name_list:
                if dir_name == target_name:
                    add_path = os.path.join(path,dir_name)
                    if not (add_path in sys.path):
                        sys.path.append(path)
                        print('* sys.path.append = '+add_path)
        if len(path)<4:
            break
except:
    traceback.print_exc()
print()