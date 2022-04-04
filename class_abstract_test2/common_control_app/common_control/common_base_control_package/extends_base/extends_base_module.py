"""
import 2
    from extends_base_common_methods import BaseClass
    import extends_base_common_methods
"""


if __name__ == '__main__':
    import extends_base_common_methods
    from extends_base_common_methods import BaseClass
else:
    from . import extends_base_common_methods
    from .extends_base_common_methods import BaseClass


class ExtendsBaseClass():
    def __init__(self,base_class:BaseClass) -> None:
        self.base_class:BaseClass=base_class
    def excute_common_methods(self):
        method_name = 'excute_common_methods'
        extends_base_common_methods.excute_common_methods(__file__,method_name,'')
        self.base_class.excute_methods(__file__,method_name,'    ')

