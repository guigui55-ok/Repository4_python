
def try_catch():
    try:
        int("aaa")
    except Exception as e:
        print(e)
        
    import traceback
    try:    
        raise ValueError("error!")
    except ValueError as e:
        print(e)
        traceback.print_exc()

try_catch()