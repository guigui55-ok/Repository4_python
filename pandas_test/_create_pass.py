

import random
_DEBUG = False
def debug_print(value):
    if _DEBUG:
        print(str(value))
ALPHABET_LIST_A = [
    'abc',
    'def',
    'ghi',
    'jkl',
    'mno',
    'pqrs',
    'tuv',
    'wxyz'
]
ALPHABET_LIST_B = [
    '2abc',
    '3def',
    '4ghi',
    '5jkl',
    '6mno',
    '7pqrs',
    '8tuv',
    '9wxyz',
    '10'
]
ALPHABET_LIST_B_LEFT = [
    '2abc',
    '3def',
    '4g',
    'qrs',
    'tv',
    'wxz',
    '1'
]
SELECT_CHAR_LIST = ALPHABET_LIST_B_LEFT
import copy

def main():
    num_list = list(range(len(SELECT_CHAR_LIST)))
    debug_print('num_list = {}'.format(num_list))

    buf_num_list = copy.copy(num_list)
    debug_print('buf_num_list = {}'.format(buf_num_list))

    ret_num_list = []
    ret_char_list = []
    for i in range(8):
        debug_print('-----')
        debug_print('count = {}'.format(i))
        n = random.choice(buf_num_list)
        ret_num_list.append(n)
        c = choice_alphabet(n)
        ret_char_list.append(c)
        debug_print('n = {}'.format(n))
        # 前後が同じ数字にならないようにする
        #/
        buf_num_list = copy.copy(num_list)
        buf_num_list.pop(n)
        debug_print('buf_num_list = {}'.format(buf_num_list))

    print('******')
    print('ret_num_list = {}'.format(ret_num_list))
    print('ret_char_list = {}'.format(ret_char_list))
    ret = ''.join(ret_char_list).capitalize()
    print('ret = {}'.format(ret))


def main2():
    num_list = list(range(len(SELECT_CHAR_LIST)))
    debug_print('num_list = {}'.format(num_list))

    buf_num_list = copy.copy(num_list)
    debug_print('buf_num_list = {}'.format(buf_num_list))

    ret_num_list = []
    ret_char_list = []
    # f
    buf_num_list.pop(1)
    for i in range(7):
        debug_print('-----')
        debug_print('count = {}'.format(i))
        n = random.choice(buf_num_list)
        ret_num_list.append(n)
        c = choice_alphabet(n)
        ret_char_list.append(c)
        debug_print('n = {}'.format(n))
        # 前後が同じ数字にならないようにする
        #/
        buf_num_list = copy.copy(num_list)
        buf_num_list.pop(n)
        debug_print('buf_num_list = {}'.format(buf_num_list))

    print('******')
    print('ret_num_list = {}'.format(ret_num_list))
    print('ret_char_list = {}'.format(ret_char_list))
    ret = 'F' + ''.join(ret_char_list)
    print('ret = {}'.format(ret))

def choice_alphabet(num):
    buf_str = SELECT_CHAR_LIST[num]
    char = random.choice(buf_str)
    return char


if __name__ == '__main__':
    # main()
    main2()