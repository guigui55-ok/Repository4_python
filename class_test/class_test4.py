"""
継承時のinit実行確認
"""


class ClassA():
    def __init__(self) -> None:
        self.value = 'AAA'
        self.value_b = 'AAA_b'
    def print_val(self):
        print(self.value)
        print(self.value_b)

class ClassInheritA(ClassA):
    def __init__(self) -> None:
        super().__init__()
        # super.__init__実行されないので、上記のように実装する
        #superを実行させずにvalue_bにアクセスするとAttributeErrorとなる
        #AttributeError: 'ClassInheritA' object has no attribute 'value_b'. Did you mean: 'value'?
        self.value = 'InheritA'
    

obj = ClassInheritA()
obj.print_val()