

class ClassA():
    def __init__(self) -> None:
        self.value = 'class_a'
    def print(self):
        print('   * ' + self.value)

class ClassAEx(ClassA):
    def print_ex(self):
        print('   * ' + self.value + ' ex')
    def print(self):
        self.print_ex()
        # return super().print()


def main():
    cl:ClassA = ClassAEx()
    cl.print()
    print(cl)

main()