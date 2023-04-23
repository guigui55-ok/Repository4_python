# https://kamatimaru.hatenablog.com/entry/2021/06/25/170126


class ExpTest():
    def __init__(self) -> None:
        self.value = 'exp_test'

class ExceptionTest3(Exception):
    def __init__(self, *args: object) -> None: ...

class TestArgs():
    def __init__(self, *args: object) -> None: ...

def main():
    cl = ExpTest()
    # raise Exception(cl)
    # raise ExceptionTest3(cl)
    ta = TestArgs('abc')
    # print(ta.args)
    return

if __name__ == '__main__':
    main()