

class Cls1():
    def __init__(self) -> None:
        self.value = 'Cls1'
    
    def print_value(self):
        print('*')
        print('value = {}'.format(self.value))
        print('id = {}'.format(id(self.value)))



class Cls2():
    value = 'Cls2'

    @classmethod
    def print_value(cls):
        print('*')
        print('value = {}'.format(cls.value))
        print('id = {}'.format(id(cls.value)))

class Cls2_2(Cls2):
    value = 'Cls2_2'

    @classmethod
    def print_value(cls):
        print('**')
        return super().print_value()