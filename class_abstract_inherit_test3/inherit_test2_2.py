#多重継承テストｓ

class NoChangeBase():
    def __init__(self) -> None:
        self.base='no_change_base'
    def print_base(self):
        print('** ' + self.base)

class NoChangeExtends():
    def __init__(self) -> None:
        self.extends='no_change_base_extends'
    def print_extends(self):
        print('** ' + self.extends)


class NoChangeMain(NoChangeExtends,NoChangeBase):
    pass


def main():
    cl = NoChangeMain()
    cl.print_extends()
    cl.print_base()

main()