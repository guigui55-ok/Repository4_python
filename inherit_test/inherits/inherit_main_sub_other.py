
if __name__ == '__main__':
    from inherit_main import InheritMain
    from inherit_other import InheritOther
else:
    from .inherit_main import InheritMain
    from .inherit_other import InheritOther 

class InheritMain(InheritOther,InheritMain):
    pass