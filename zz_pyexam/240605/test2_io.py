import io

def io_test1():
    s = io.StringIO('Hello, world!')
    s.close()

    result = s.getvalue()
    print(result)

def io_test2():
    s = io.StringIO('Hello, world!')

    result = s.getvalue()
    s.close()
    print(result)

def io_test3():
    import io

    s = io.StringIO()
    s.write('ham\n')
    s.seek(0)
    s.write('egg')

    print(s.getvalue())

if __name__ == '__main__':
    io_test3()