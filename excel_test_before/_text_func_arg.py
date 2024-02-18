
class Const():
    VALUE = 1
    def __new__(cls) -> None:
        cls.VALUE = 3
        


class TestClass():
    class Const(Const):
        pass
    def __init__(self) -> None:
        self.value = self.Const.VALUE
    
    # def excute(self, value=TestClass.Const.VALUE): #NameError: name 'TestClass' is not defined
    #     print(value)
    # def excute(self, value=self.value): #name 'self' is not defined
    #     print('# value = {}'.format(value))

    def excute(self, value=Const.VALUE):
        print('# value = {}'.format(value))

Const.VALUE = 2
TestClass.Const.VALUE = 2
test_class = TestClass()
test_class.excute()