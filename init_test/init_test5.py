"""
from init_test_m2 import init_test_m2
import init_test3（init_test_m2をimportしている）
from init_test_m2_3 import init_test_m2_3
を読み込んだ時、__initは読み込まれるか、挙動を確認

"""
from init_test_m2 import init_test_m2
#同じモジュールを読み込むのは1回だけ
from init_test_m2 import init_test_m2

import init_test3
from init_test_m2 import init_test_m2_3

def import_module():
    print('** import_module')
    #同じモジュールを読み込むのは1回だけ
    from init_test_m2 import init_test_m2

def main():
    print('** main')
    print('    ' + __name__)
    import_module()
    print('** init_test3.main')
    init_test3.main()

if __name__ == '__main__':
    main()