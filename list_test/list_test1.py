


def main():
    list_a = ['a','b','c','d']

    print('*****')
    for val in list_a:
        if 'b' in val:
            val = 'BB'
        # if 'a' in val:
        #     val = 'AA'
        print(id(val))
    print(list_a)
    print('*****')
    for i in range(len(list_a)):
        print(id(list_a[i]))
    return




if __name__ == '__main__':
    main()