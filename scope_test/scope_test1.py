from operator import mod
import traceback

bar = '##################################################'

try:
    import module_a

    print(module_a.module_a_a1)
    #例外が発生しました: AttributeError
    #module 'module_a' has no attribute 'module_a_a1'
except:
    traceback.print_exc()
    print()
    print(bar)

try:
    from module_a import module_a1
    print(module_a1.var_a1)
    module_a1.var_a1 = 2
    print(module_a1.var_a1)

    from module_a.module_a_a import module_a_a1
    print(module_a_a1.var_a1)

    from module_a.module_a_a.module_a_a1 import var_a_a1
    from module_a.module_a1 import var_a_a1
    print(var_a_a1) # 最後のもので上書きされる
except:
    traceback.print_exc()
    print()
    print(bar)

try:
    print(bar)
    from module_a.module_a1 import var_a_a1 as var1
    print(var1)
    var1 = 'var1'
    print(var1)
    print(id(var1))
    from module_a.module_a1 import var_a_a1 as var1_2
    print(var1_2)
    print(id(var1_2))
    #別アドレスとなる、新たに宣言されたと同じととらえてよい
except:
    traceback.print_exc()
    print()
    print(bar)


def module_var_test(module_var):
    print('---')
    mod_a_local = module_var
    print(id(mod_a_local))
    mod_a_local.module_a1.var_a_a1 = 'ddd'
    print(mod_a_local.module_a1.var_a_a1)
    print(module_var.module_a1.var_a_a1)

try:
    print(bar)
    import module_a as mod_a
    print(type(mod_a))
    print(id(mod_a))
    mod_a.module_a1.var_a_a1 = 'abc'
    print(mod_a.module_a1.var_a_a1)
    print(mod_a)
    print(mod_a.__path__)
    print(mod_a.__file__)
    print(mod_a.__doc__)

    print('---')
    import module_a as mod_a
    print(type(mod_a))
    print(id(mod_a))
    print(mod_a.module_a1.var_a_a1)
    #再度同じ構文でインポートしたときは、メモリアドレスは同一
    #再度インポートする前の、モジュールのグローバル変数変数の変更は保持されており
    #インポート時に上書きされない
    print('---')
    from scope_test1_1 import module_a as mod_a
    print(id(mod_a))
    print(mod_a.module_a1.var_a_a1)
    print('---')
    from scope_test1_1 import module_a as mod_a_2
    print(id(mod_a_2))
    print(mod_a_2.module_a1.var_a_a1)
    print('---')
    mod_a_local = mod_a
    print(id(mod_a_local))
    mod_a_local.module_a1.var_a_a1 = 'ccc'
    print(mod_a_local.module_a1.var_a_a1)
    module_var_test(mod_a)
    print(mod_a.module_a1.var_a_a1)

except:
    traceback.print_exc()
    print()
    print(bar)

