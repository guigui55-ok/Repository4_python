from abc import ABCMeta, abstractmethod

class Prototype(metaclass=ABCMeta):
    def __init__(self) -> None:
        self.classname = 'Prototype'
    @abstractmethod
    def print_classname(self):
        print('AbstractClass1')
    @abstractmethod
    def test_method_abc(self):
        print(self.classname + '.test_method_abc')

class MassProduction(Prototype):
    def __init__(self) -> None:
        super().__init__()
        self.classname = 'MassProduction'
    def print_classname(self):
        print('name=MassProduction')
    def original_method(self):
        print('MassProduction original')
    def test_method_abc(self):
        return super().test_method_abc()

class MassProduction_b(Prototype):
    def __init__(self) -> None:
        super().__init__()
        self.classname = 'MassProduction_b'
    def print_classname(self):
        print('name=MassProduction_b')
    def original_method_b(self):
        print('MassProduction_b original')
    def test_method_abc(self):
        return super().test_method_abc()

def get_object(mode:int):
    if mode == 1:
        return MassProduction()
    elif mode == 2:
        return MassProduction_b()
    else:
        return None
        raise Exception()
    

def main():
    # pro = Prototype()
    #TypeError: Can't instantiate abstract class Prototype with abstract method print_classname
    # mas:Prototype = MassProduction()

    # print_classnameメソッドを実装していないときエラーとなる
    # Can't instantiate abstract class MassProduction with abstract method print_classname

    #intellisenceが効くかのテスト
    #両方とも参照したい→OK
    mas = get_object(2)
    if isinstance(mas,MassProduction_b):
        mas.original_method_b()
    else:
        mas.original_method()
    mas.print_classname()



main()
