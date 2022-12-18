


class OverRideTest():
    def __init__(self) -> None:
        print('OverRideTest __init__')
        self.name = self.__class__
        print(f'self.__class__.__name__ = {self.__class__.__name__}')
        if self.__class__.__name__ == 'OverRideTest':
            raise Exception()

    @classmethod
    def create_instance(self, value):
        if value==1:
            return OverRideTestA()
        else:
            return OverRideTestB()

    def print_test(self):
        print('OverRideTest')


class OverRideTestA(OverRideTest):
    def __init__(self) -> None:
        super().__init__()
    def print_test(self):
        print('OverRideTestA')

class OverRideTestB(OverRideTest):
    def __init__(self) -> None:
        super().__init__()
    def print_test(self):
        print('OverRideTestB')

def main():
    obj = OverRideTest()
    obj = OverRideTest.create_instance(1)
    obj.print_test()
    return

if __name__ == '__main__':
    main()