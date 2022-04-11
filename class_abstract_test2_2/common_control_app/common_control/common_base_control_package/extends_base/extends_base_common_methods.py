"""
import 1
from base_package.base_module import BaseClass as BaseClass

"""
if __name__ == '__main__':
    import __init__
from base_package.base_module import BaseClass


def excute_common_methods(base_class:BaseClass,called_file_path:str,called_method_name:str):
    print('excute_common_methods')
    print('    * ' + __file__)
    indent = '    '
    BaseClass.excute_methods(BaseClass,called_file_path,called_method_name,indent)
    # print(indent + 'called')
    # print(indent + 'path  > '+ called_file_path)
    # print(indent + 'metod > '+ called_method_name)