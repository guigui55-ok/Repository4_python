
"""
import 3
import extends_base_module
from extends_base_module import ExtendsBaseClass
"""


# if __name__ == '__main__':
#     import extends_base.init_import
# else:
#     import extends_base.init_import
import init_import
if __name__ == '__main__':
    import common_base_control_package
    from common_base_control_package.extends_base.extends_base_module import ExtendsBaseClass
else:
    from . import common_base_control_package
    from .common_base_control_package.extends_base.extends_base_module import ExtendsBaseClass
# from . import common_base_control_package # attempted relative import with no known parent package
# from . import common_base_control_package
# import common_base_control_package.extends_base.extends_base_module
# #  extends_base.extends_base_module
# # import common_control.common_base_control_package.extends_base.extends_base_module
# from common_control.common_base_control_package.extends_base.extends_base_module import ExtendsBaseClass

class CommonActionBase():
    def __init__(self,ext_base:ExtendsBaseClass) -> None:
        self.extends_base_class:ExtendsBaseClass = ext_base
    
    def excute(self):
        indent = '    '
        print('CommonActionBase.excute')
        print('    * ' + __file__)
        self.extends_base_class.excute_common_methods()