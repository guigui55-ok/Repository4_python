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
    pass


def main():
    cl = NoChangeMain()
    cl.print_extends()
    cl.print_base()

main()