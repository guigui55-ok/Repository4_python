

class Prototype():
    def __init__(self) -> None:
        self.classname = 'Prototype'
    def print_classname(self):
        print('Prototype')

class MassProduction(Prototype):
    def __init__(self) -> None:
        super().__init__()
        self.classname = 'MassProduction'
    def print_classname(self):
        print('name=MassProduction')
    def original_method(self):
        print('MassProduction original')

class MassProduction_b(Prototype):
    def __init__(self) -> None:
        super().__init__()
        self.classname = 'MassProduction_b'
    def print_classname(self):
        print('name=MassProduction_b')
    def original_method_b(self):
        print('MassProduction_b original')

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
    mas = get_object(1)
    if isinstance(mas,MassProduction_b):
        mas.original_method_b()
    else:
        mas.original_method()
    mas.print_classname()

def check_object_type(maspro):
    if isinstance(maspro,MassProduction) or isinstance(maspro,MassProduction_b):
        return maspro

def test_inherit2(maspro):
    #intellisenceが効くかのテスト
    #両方とも参照したい→isinstanceを通したメソッドおっでもOK
    maspro = check_object_type(maspro)
    mas = maspro
    if isinstance(mas,MassProduction_b):
        mas.original_method_b()
    else:
        mas.original_method()
    mas.print_classname()

def test_inherit(maspro):
    #intellisenceが効くかのテスト
    #両方とも参照したい→isinstanceを通すとOK
    if isinstance(maspro,MassProduction_b):
        maspro.original_method_b()
    elif isinstance(maspro,MassProduction):
        maspro.original_method()
    else:
        maspro.original_method()
    if isinstance(maspro,MassProduction) or isinstance(maspro,MassProduction_b):
        maspro.print_classname()


main()
