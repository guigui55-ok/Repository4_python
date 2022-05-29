

if __name__ == '__main__':
    from inherit_other import InheritAnother
else:
    from .inherit_other import InheritAnother


class InheritMain(InheritAnother):
    pass