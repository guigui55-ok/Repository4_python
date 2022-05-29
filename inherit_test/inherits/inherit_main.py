

if __name__ == '__main__':
    from inherit_other import InheritOther
else:
    from .inherit_other import InheritOther


class InheritMain():
    def __init__(self) -> None:
        self.other = InheritOther()
    def excute(self):
        print('Excute InheritMaine')

if __name__ == '__main__':
    InheritMain().excute()