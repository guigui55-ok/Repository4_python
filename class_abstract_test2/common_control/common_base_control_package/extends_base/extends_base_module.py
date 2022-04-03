"""
import 2
    from extends_base_common_methods import BaseClass
    import extends_base_common_methods
"""


if __name__ == '__main__':
    from extends_base_common_methods import BaseClass
    import extends_base_common_methods
else:
    from common_base_control_package.extends_base.extends_base_common_methods import BaseClass
    import common_base_control_package.extends_base.extends_base_common_methods


class ExtendsBaseClass():
    def __init__(self,base_class:BaseClass) -> None:
        self.base_class:BaseClass=base_class
    def excute_common_methods(self):
        method_name = 'excute_common_methods'
        extends_base_common_methods.excute_common_methods(__file__,method_name,'')
        self.base_class.excute_methods(__file__,method_name,'    ')

