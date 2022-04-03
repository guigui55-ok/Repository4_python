
# 引数で渡すとき、参照渡しとなるか
import traceback

# class ClassTest3():
#     def __init__(self,value) -> None:
#         self.value = value
#     def output(self):
#         print(self.value)

def show_id(str_object):
    print('---')
    print('str_object = '+str_object)
    print(id(str_object))
    str_object = 'str1-2'
    print(id(str_object))

import _ctypes
def get_value_from_id(str_object):
    print('---')
    print('str_object = '+str_object)
    val_id = id(str_object)
    print(val_id)
    str_object = 'str1-2'
    print(id(str_object))
    print('---')
    import _ctypes
    test_from_id = _ctypes.PyObj_FromPtr(val_id)
    test_from_id = 'str_change'
    print(test_from_id)
    print(type(test_from_id))
    print(id(test_from_id))

def main():
    try:
        str_1 = 'str_1'
        str_1.__str__
        print('str_1 = '+str_1)
        print(id(str_1))
        show_id(str_1)
        get_value_from_id(str_1)
        print('---')
        print('str_1 = '+str_1)
        print(id(str_1))
    except:
        traceback.print_exc()


if __name__ == '__main__':
    main()