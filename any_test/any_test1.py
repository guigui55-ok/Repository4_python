
from pyparsing import anyCloseTag


class any_class():
    def __init__(self) -> None:
        self.value = 'any_class_value'
    def excute(self):
        print('excute')


def main():
    cl = any_class()
    cl.excute()
    t:type = type(cl)
    # print(t.excute(t)) #any_class().excute() と同じ
    # type(any_class()) == any_class()
    
main()