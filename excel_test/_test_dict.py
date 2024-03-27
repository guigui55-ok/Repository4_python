

# class TestClass():
#     def __init__(self, value='') -> None:
#         self.value = ''
#     def print_value(self):
#         print(self.value)

# value = 'val'
# d = {'value': value}

# print('d = ')
# print(d)
# print('d.__str__= ')
# print(d.__str__())
# print('d.values= ')
# print(d.values())

class StrObject(str):
    """
    """
    def __init__(self, object=None) -> None:
        super().__init__()
        self.__str__()
        if not isinstance(object, str):
            self.object = object
        else:
            self.object = None
    
    def print_values(self):
        print(type(self))
        print(self)
        print(type(self.object))
        print(self.object)

buf = StrObject('abc')
from pathlib import Path
print('---')
buf = StrObject('abc')
buf.print_values()
print('---')
buf = StrObject('abc')
buf.object = int(2)
buf.print_values()
print('---')
buf = StrObject(Path(__file__))
buf.print_values()