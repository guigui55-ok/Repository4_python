
class class_test1():
    value1:str = ''
    value2:int = ''
    def __init__(self,arg1:str,arg2:int):
        self.value1 = arg1
        self.value2 = arg2
    #self.value3 = 'val3'
    # 例外が発生しました: NameError
    # name 'self' is not defined
    __value4 = 'value4'
    # クラスメソッド.
    @classmethod
    def class_method(cls):
        print('class_method')
        # インタンス化していないクラスのものから呼び出せます。
    # プライベートメソッド
    def __MyCalc(self):
        print ("This is Private Method!")

def class_test1_method():

    class_test1.class_method()
    # class_test1.__MyCalc()
    # 例外が発生しました: AttributeError
    # type object 'class_test1' has no attribute '__MyCalc'

    c = class_test1('val1',2)
    print('value1 = '+ c.value1)
    #print(c.value3)
    # print('__value4 = '+ c.__value4)
    # 例外が発生しました: AttributeError
    # 'class_test1' object has no attribute '__value4'

if __name__ == '__main__':
    class_test1_method()