"""
240503

スーパークラスのメソッド実行時に、継承先のクラスのselfを使うテスト
"""

class BaseClassA():
    def __init__(self) -> None:
        self.base_a_value = 'base_a_value'
    
    def print_test_a(self):
        print(self.base_a_value)

    def print_other_b(self):
        self.print_test_b()

    def print_other_b_direct(self):
        print(self.base_b_value)

class BaseClassB():
    def __init__(self) -> None:
        self.base_b_value = 'base_b_value'
    
    def print_test_b(self):
        print(self.base_b_value)
        

class TestClass(BaseClassA, BaseClassB):
    def __init__(self) -> None:
        # super().__init__()# ClassAのコンストラクタしか呼ばれない
        BaseClassA.__init__(self)  # BaseClassAのコンストラクタを呼び出す
        BaseClassB.__init__(self)  # BaseClassBのコンストラクタを呼び出す

def main():
    obj = TestClass()
    obj.print_test_a()
    obj.print_test_b()
    obj.print_other_b()
    obj.print_other_b_direct()

if __name__ == '__main__':
    main()