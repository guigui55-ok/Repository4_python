

import package1


import sys

from package1.module1_1 import class1_1, module1_1
from package1.package1_2.module1_2 import class1_2
sys.path.append('/')
# import pacakge2
# from .package1 import 1_3package

print('import_test done')
module1_1
c1type = module1_1.__class__
print(c1type)
c1 = class1_1()
buf = c1.get_class_name()
print('c1.get_class_name=' + str(buf))
print('c1.get_class_name=' + str(class1_1().get_class_name()))

c2 = class1_2
buf = c2.get_class_name()
print('c2.get_class_name=' + str(buf))