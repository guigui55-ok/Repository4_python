
class Const():
    VALUE = 1
    def __new__(cls) -> None:
        cls.VALUE = 3
        


class TestClass():
    class ConstB(Const):
        pass
    def __init__(self) -> None:
        self.value = self.ConstB.VALUE
    
    # def excute(self, value=TestClass.Const.VALUE): #NameError: name 'TestClass' is not defined
    #     print(value)
    # def excute(self, value=self.value): #name 'self' is not defined
    #     print('# value = {}'.format(value))

    def excute(self, value=ConstB.VALUE):
        print('# value = {}'.format(value))

class TestClassB(TestClass):
    class ConstB(Const):
        VALUE = 11

Const.VALUE = 2
TestClass.ConstB.VALUE = 2
test_class = TestClass()
test_class.excute()
test_class = TestClassB()
test_class.excute()