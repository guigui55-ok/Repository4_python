print('module2_2')

class class2_2:
    cls_name = 'class2_2'
    print('class class2_2 do')
    def get_class_name(self):
        return 'get_class_name(self) : ' + self.cls_name
    def get_class_name():
        # static method なので、クラス変数にはアクセスできず、エラーとなる
        # return 'get_class_name() : ' + self.cls_name
        return 'get_class_name() : class2_2'

class class2_2_sub1:
    print('class2_2_sub1 begin')
    def __init__(self):
        print('class class2_2_sub1 constracta')

    def get_class_name(self):
        return 'get_class_name(self) : class2_2_sub1'

def module2_2():
    print('def module2_2 do')