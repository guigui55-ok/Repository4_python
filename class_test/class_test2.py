
import traceback


class Test2():
    def __init__(self) -> None:
        self.val = 'val'


def class_test2():
    try:
        c = Test2()
        print(c.val)
        return
    except:
        traceback.print_exc()


def main():
    class_test2()
main()