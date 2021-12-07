
# def args_as_function(func:function,args): # NameError: name 'function' is not defined
def args_as_function(func,args):
    try:
        print('type(func) = ' + str(type(func)))
        func(args)
    except:
        import traceback
        print(traceback.print_exc())
        return

def called_function(args):
    try:
        print('called_function : ' + str(args) )
        return True
    except:
        import traceback
        print(traceback.print_exc())
        return False

def main():
    try:
        args_as_function(called_function,'test_str')
        return
    except:
        import traceback
        print(traceback.print_exc())
        return

main()