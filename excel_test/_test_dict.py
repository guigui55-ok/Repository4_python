

class TestClass():
    def __init__(self, value='') -> None:
        self.value = ''
    def print_value(self):
        print(self.value)

value = 'val'
d = {'value': value}

print('d = ')
print(d)
print('d.__str__= ')
print(d.__str__())
print('d.values= ')
print(d.values())