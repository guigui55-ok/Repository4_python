def my_generator():
    yield 1
    yield 2
    yield 3

g = my_generator()
next(g)
next(g)
next(g)
next(g)