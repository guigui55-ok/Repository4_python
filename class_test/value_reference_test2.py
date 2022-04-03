
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

def main():
    try:
        str_1 = 'str_1'
        show_id(str_1)
        str_1 = 'str_1'
        show_id(str_1)
        str_1 = 'str_2'
        show_id(str_1)
        str_1 = 'str_12'
        show_id(str_1)
        str_1 = 'str_12'[:-1]
        show_id(str_1)
        
    except:
        traceback.print_exc()


if __name__ == '__main__':
    main()