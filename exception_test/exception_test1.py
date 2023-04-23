



class TestClass():
    def __init__(self) -> None:
        self.value = 'test_class'



class TestException(Exception):
    def __init__(self, *args: object) -> None:
        print('*** TestException')
        for arg in args:
            print('type arg = {}'.format(type(arg)))
        super().__init__(*args)


def main():
    raise TestException({})



if __name__ == '__main__':
    print()
    print('*****')
    main()