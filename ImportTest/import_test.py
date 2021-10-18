

import package1
import sys
sys.path.append('/')

# import 列挙して一度に import が可能
from package1.module1_1 import class1_1, module1_1

# 下位 ディレクトリ(package) の import
from package1.package1_2.module1_2 import class1_2

# 先頭に数字を使うと import ができず、SyntaxError: invalid syntax となる
# from package1.1_3package import class1_3_1
# from .package1 import 1_3package

# __init__.py(中身は空でOK)がpapckage(Package2 folder)直下にないと、import error となる(python v3.3以下)
# from Package2.Package2_2 import class2_2
# # import Pacakge2
import Package2.Package2_2.module2_2
from Package2.Package2_2.module2_2 import class2_2, class2_2_sub1

print('import_test done')
module1_1
c1type = module1_1.__class__
print('module1_1.__class__ = ' + str(c1type))
c1 = class1_1()
buf = c1.get_class_name()
print('c1.get_class_name = ' + str(buf))
print('c1.get_class_name = ' + str(class1_1().get_class_name()))

c2 = class1_2()
buf = c2.get_class_name(c2)
print('c2.get_class_name = ' + str(buf))
buf = class1_2.get_class_name()
print('c2.get_class_name = ' + str(buf))

# インスタンス生成しないパターン
c2_2 = class2_2
buf = c2_2.get_class_name()
print('c2_2.get_class_name() = ' + str(buf))
buf = class2_2.get_class_name()
print('c2_2.get_class_name() = ' + str(buf))

# 以下は className() かっこがない状態での代入で、get_class_name実行時にエラーとなる
# c2_2_sub1 = class2_2_sub1
# buf = c2_2_sub1.get_class_name()
# 以下が正しい
c2_2_sub1 = class2_2_sub1()
buf = c2_2_sub1.get_class_name()
print('c2_2_sub1.get_class_name() = ' + str(buf))
# c1_3_1 = class1_3_1