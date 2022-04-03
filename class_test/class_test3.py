
# 引数で渡すとき、参照渡しとなるか
import traceback

class ClassTest3():
    def __init__(self,value) -> None:
        self.value = value
    def output(self):
        print(self.value)

def show_id(class_object):
    print('---')
    class_object.output()
    print(id(class_object))
    print('---')
    class_object.value = 'class3-2'
    class_object.output()
    print(id(class_object))

def main():
    try:
        cl = ClassTest3('class3')
        cl.output()
        print(id(cl))
        show_id(cl)
        print('---')
        cl.output()
        print(id(cl))
    except:
        traceback.print_exc()


if __name__ == '__main__':
    main()