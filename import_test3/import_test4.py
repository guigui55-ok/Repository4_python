
try:
    import dummy
except Exception as e:
    print(str(e))
    print(e.__traceback__)
    import inspect
    frame = inspect.currentframe()
    print(frame.f_code.co_filename, ':line',frame.f_lineno)
    import traceback
    traceback.print_exc()