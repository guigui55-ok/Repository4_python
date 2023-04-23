


BUF_LIST = [1,2,4,8,16]

def main():
    # OK
    for index, x in enumerate(BUF_LIST):
        print('index={}, x={}'.format(index, x))
    print('---')
    # OK
    for x in BUF_LIST:
        print(x+1)

if __name__ == '__main__':
    print()
    print('****')
    main()