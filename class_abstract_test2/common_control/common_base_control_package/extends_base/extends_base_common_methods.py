"""
import 1
import init_import
from base_package.base_module import BaseClass as BaseClass

"""
if __name__ == '__main__':
    import init_import
else:
    # from . import init_import
    from common_base_control_package.extends_base import init_import

from base_package.base_module import BaseClass as BaseClass


def excute_common_methods(base_class:BaseClass,called_file_path:str,called_method_name:str):
    print('excute_common_methods')
    print('    * ' + __file__)
    indent = '    '
    BaseClass.excute_methods(BaseClass,called_file_path,called_method_name,indent)
    # print(indent + 'called')
    # print(indent + 'path  > '+ called_file_path)
    # print(indent + 'metod > '+ called_method_name)