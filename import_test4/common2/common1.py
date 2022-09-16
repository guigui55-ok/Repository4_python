
print(__file__[__file__[:__file__.rfind('\\')-1].rfind('\\'):])

if __name__ == '__main__':
    from __init__ import NUMBER
else:
    # from common2.__init__ import NUMBER
    # from common1 import NUMBER
    from __init__ import NUMBER

def common_function():
    print('common_function 2 ' + NUMBER)

class CommonClass():
    def __init__(self) -> None:
        print('CommonClass 2 ' + NUMBER)
    def excute(self):
        print('excute 2' + NUMBER)