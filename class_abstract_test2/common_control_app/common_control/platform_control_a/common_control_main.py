
"""
import 4
import extends_base_module
from extends_base_module import ExtendsBaseClass
"""

import init_import
if __name__ == '__main__':
    import common_base_control_package
    from common_base_control_package.extends_base.extends_base_module import ExtendsBaseClass
    from common_control_base.common_control_main import CommonActionBase
else:
    import common_base_control_package
    from common_base_control_package.extends_base.extends_base_module import ExtendsBaseClass
    from common_control_base.common_control_main import CommonActionBase
    

class CommonActionBase_A(CommonActionBase):
    def __init__(self,ext_base:ExtendsBaseClass) -> None:
        self.extends_base_class:ExtendsBaseClass = ext_base
    
    def excute(self):
        indent = '    '
        print('CommonActionBase.excute')
        print('    * ' + __file__)
        self.extends_base_class.excute_common_methods()