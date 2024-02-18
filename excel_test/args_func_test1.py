"""
引数に関数が渡される関数について
 引数を複数持つ関数が渡されるときについて
"""

# 一つの方法は、args_test_func に追加の引数を受け取るようにし、これらの引数を func に渡すようにすることです。以下に例を示します：

def multi_args_func(arg_a, arg_b):
    print('arg_a = {}, arg_b={}'.format(str(arg_a), str(arg_b)))

def args_test_func(func, *args, **kwargs):
    func(*args, **kwargs)

args_test_func(multi_args_func, 'aaa', 'bbb')
# ここで、args_test_func は func に渡すための位置引数 (*args) とキーワード引数 (**kwargs) を受け取ります。この関数は受け取った引数を func に渡します。この例では multi_args_func に2つの位置引数 'aaa' と 'bbb' を渡しています。
# 別の方法として、multi_args_func を args_test_func に渡す前に部分適用（partial application）を使って引数をバインドすることもできます。これは functools.partial を使用して行うことができます：

from functools import partial

def multi_args_func(arg_a, arg_b):
    print('arg_a = {}, arg_b={}'.format(str(arg_a), str(arg_b)))

def args_test_func(func):
    func()

# 部分適用を使用して引数をバインド
partial_func = partial(multi_args_func, 'aaa', 'bbb')

args_test_func(partial_func)
# この例では、partial(multi_args_func, 'aaa', 'bbb') が multi_args_func のバージョンを作成し、'aaa' と 'bbb' がその引数として既にバインドされています。その後、この部分適用された関数を args_test_func に渡します。


### バインドした関数の引数を部分的に変更

from functools import partial

def multi_args_func(arg_a, arg_b):
    print('arg_a = {}, arg_b={}'.format(str(arg_a), str(arg_b)))

# 元の部分適用関数
partial_func = partial(multi_args_func, 'aaa', 'bbb')

# 'bbb' を 'ccc' に変更するために再度 partial を使用
new_partial_func = partial(partial_func.func, *partial_func.args[:-1], 'ccc')

# 新しい部分適用関数を実行
new_partial_func()


