#先頭部分に処理を書いたときの挙動確認

import datetime
class TestClass5():

    print("TestClass5 Process")
    buf_date_str = datetime.datetime.now().strftime("%Y/%m/%D %H:%M:%S %F")
    buf_calc_value = 10+21
    
    def __init__(self):
        pass

    def execute(self):
        print('buf_date_str = {}'.format(self.buf_date_str))
        print('buf_calc_value = {}'.format(self.buf_calc_value))


if __name__ == '__main__':
    print("*****")
    test_class_obj = TestClass5()
    test_class_obj.execute()