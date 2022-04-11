# import pathlib
# path = str(pathlib.Path(__file__).parent)
# print('__ '+ path)


"""
    target_name_list =['base_package','common_general','class_abstract_test2']
"""
is_excute = False
print(is_excute)
if not is_excute:
    is_excute = True
print('######################################################################')
print('* '+__file__)
import sys,os,pathlib
import traceback

def sys_path_append_if_not_exists(add_path:str):
    if not (add_path in sys.path):
        sys.path.append(path)
        print('* sys.path.append = '+add_path)
try:
    target_name_list =['base_package','common_general','class_abstract_test2','common_control','common_base_control_package']
    path = str(pathlib.Path(__file__))
    # sys_path_append_if_not_exists(str(pathlib.Path(__file__).parent))
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
                    sys_path_append_if_not_exists(add_path)
        if len(path)<4:
            break
except:
    traceback.print_exc()
print()
# print('**** ' + __file__)
# for p in sys.path:
#     print(p)



# from base_package.base_module import BaseClass
# import common_general
