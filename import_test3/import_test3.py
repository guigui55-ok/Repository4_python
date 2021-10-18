# 同じパッケージ名/異なるモジュール名/同じクラス名 を実行する

import package6
from package6.module6_1 import class6_1, method6
from package7.module7 import method7

# c = class6()
# 例外が発生しました: NameError       (note: full exception trace is shown but execution is paused at: <module>)
# name 'class6' is not defined

c = class6_1()

# package6 モジュールを import する
from package6.module6_1 import class6 as module6_1_class6
c = module6_1_class6()

# 元のモジュールで同名のオブジェクト定義があっても、別名としてならインポートできる
from package6.module6_2 import class6 
c = class6()

# function でもクラスと同じ
from package6.module6_1 import method6 as module6_1_method6
module6_1_method6()
from package6.module6_2 import method6
method6()

# import package7
method7()
