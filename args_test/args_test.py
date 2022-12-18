


def func(**kwargs):
    # print(type(**kwargs))
    # print(**kwargs)
    print(type(kwargs))
    print(kwargs)

def main():
    func(dict_args = {'dict':'d_value'})
    return


if __name__ =='__main__':
    main()