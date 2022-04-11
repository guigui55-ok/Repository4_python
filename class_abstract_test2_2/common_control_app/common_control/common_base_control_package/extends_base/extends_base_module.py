"""
import 2
    from base_package.base_module import BaseClass
    import extends_base_common_methods
"""


if __name__ == '__main__':
    import __init__
    import extends_base_common_methods
else:
    from . import extends_base_common_methods
from base_package.base_module import BaseClass


class ExtendsBaseClass():
    def __init__(self,base_class:BaseClass) -> None:
        self.base_class:BaseClass=base_class
    def excute_excute_method_base_class(self):
        method_name = 'excute_excute_method_base_class'
        self.base_class.excute_methods(__file__,method_name,'    ')

    def excute_excute_method_by_common_methods(self):
        method_name = 'excute_excute_method_by_common_methods'
        extends_base_common_methods.excute_common_methods(__file__,method_name,'')

