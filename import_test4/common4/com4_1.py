

def main():
    print(__file__[__file__[:__file__.rfind('\\')-1].rfind('\\'):])
    print('main')
    return

if __name__ == '__main__':
    main()