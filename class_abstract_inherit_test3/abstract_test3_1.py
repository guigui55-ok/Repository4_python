from abc import ABCMeta, abstractmethod

class Prototype(metaclass=ABCMeta):
    def __init__(self) -> None:
        self.classname = 'Prototype'
    @abstractmethod
    def print_classname(self):
        print('AbstractClass1')

class MassProduction(Prototype):
    def __init__(self) -> None:
        super().__init__()
        self.classname = 'MassProduction'
    def print_classname(self):
        print('name=MassProduction')
    def original_method(self):
        print('MassProduction original')


def main():
    # pro = Prototype()
    #TypeError: Can't instantiate abstract class Prototype with abstract method print_classname
    mas = MassProduction()

    # print_classnameメソッドを実装していないときエラーとなる
    # Can't instantiate abstract class MassProduction with abstract method print_classname



main()
