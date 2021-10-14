
import module1
import module2

from module2 import func
from module1 import func
# as で　リネームできる
from module2 import func as func2
from module1 import func as func1
from module1 import test_class as test_class1
# 後から import したほうが実行される
from module1 import module1_func, test_class
from module2 import test_class

func()
test_class()
module1_func()
func1()
func2()
test_class1()