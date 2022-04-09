#多重継承テスト

class NoChangeBase():
    def print_base(self):
        self.base='no_change_base'
        print('** ' + self.base)

class NoChangeExtends():
    def print_extends(self):
        self.extends='no_change_base_extends'
        print('** ' + self.extends)


class NoChangeMain(NoChangeExtends,NoChangeBase):
    def __init__(self) -> None:
        super().__init__()
        print('NoChangeMain 2')


class NoChangeExtends_b():
    def print_extends_b(self):
        self.extends='no_change_base_extends_b'
        print('** ' + self.extends)


class NoChangeMain(NoChangeExtends_b,NoChangeExtends,NoChangeBase):
    def __init__(self) -> None:
        super().__init__()
        print('NoChangeMain 3')


def main():
    cl = NoChangeMain()
    cl.print_extends()
    cl.print_base()
    cl.print_extends_b()

main()