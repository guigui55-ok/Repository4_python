from abc import ABCMeta, abstractmethod

class AbstractClass1(metaclass=ABCMeta):
    def __init__(self) -> None:
        self.classname = 'AbstractClass1'
    @abstractmethod
    def print_classname(self):
        print('AbstractClass1')

class ExcuterClass(AbstractClass1):
    pass

def main():
    try:
        cl = ExcuterClass()
        cl.print_classname()
        return
    except:
        import traceback
        traceback.print_exc()

if __name__ == '__main__':
    main()
