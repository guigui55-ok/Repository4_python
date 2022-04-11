
"""
import 3
import extends_base_module
from extends_base_module import ExtendsBaseClass
"""


if __name__ == '__main__':
    import __init__
    import common_base_control_package
    from common_base_control_package.extends_base.extends_base_module import ExtendsBaseClass
else:
    import common_base_control_package
    from common_base_control_package.extends_base.extends_base_module import ExtendsBaseClass

class CommonActionBase():
    def __init__(self,ext_base:ExtendsBaseClass) -> None:
        self.extends_base_class:ExtendsBaseClass = ext_base
    
    def excute_by_common_methods(self):
        indent = '    '
        print('CommonActionBase.excute_by_common_methods')
        print('    * ' + __file__)
        self.extends_base_class.excute_excute_method_by_common_methods()
    def excute_by_base_class(self):
        indent = '    '
        print('CommonActionBase.excute_by_base_class')
        print('    * ' + __file__)
        self.extends_base_class.excute_excute_method_base_class()