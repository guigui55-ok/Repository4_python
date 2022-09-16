
print(__file__[__file__[:__file__.rfind('\\')-1].rfind('\\'):])

if __name__ == '__main__':
    from __init__ import NUMBER
else:
    from common1.__init__ import NUMBER

def common_function():
    print('common_function ' + NUMBER)

class CommonClass():
    def __init__(self) -> None:
        print('CommonClass' + NUMBER)
    def excute(self):
        print('excute ' + NUMBER)