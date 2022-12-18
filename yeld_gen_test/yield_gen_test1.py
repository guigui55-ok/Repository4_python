# https://qiita.com/keitakurita/items/5a31b902db6adfa45a70

def fibonacci():
    a, b = 0, 1
    while 1:
        print(f'b={b}')
        yield b
        a, b = b, a+b


def main():
    f = fibonacci()
    for val in f:
        print(val)
    return


if __name__ == '__main__':
    main()