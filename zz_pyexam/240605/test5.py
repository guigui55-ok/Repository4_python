from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('calling decorated function')
        return func(*args, **kwargs)
    return wrapper


@my_decorator
def my_decorated_func():
    """this is my decorated func"""
    print('inside function')
    print(my_decorated_func.__name__)
    print(my_decorated_func.__doc__)

my_decorated_func()
