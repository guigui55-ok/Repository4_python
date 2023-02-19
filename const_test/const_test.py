

class Const():
    CONST = 'const'


class ConstB():
    CONST = 'constB'
    def __init__(self) -> None:
        self.CONST = 'constB_member'


def main():
    con = ConstB
    print('CONST ={}'.format(con.CONST))
    print('id={}'.format(id(con.CONST)))
    con.CONST = 'change'
    print('CONST m ={}'.format(con.CONST))
    print('id={}'.format(id(con.CONST)))
    print('CONST c ={}'.format(ConstB.CONST))
    print('id={}'.format(id(ConstB.CONST)))
    con = ConstB()
    print('CONST m ={}'.format(con.CONST))
    print('id={}'.format(id(con.CONST)))
    print('CONST c ={}'.format(ConstB.CONST))
    print('id={}'.format(id(ConstB.CONST)))


if __name__ == '__main__':
    main()