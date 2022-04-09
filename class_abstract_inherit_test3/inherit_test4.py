# https://fereria.github.io/reincarnation_tech/10_Programming/00_Python/10_Python2/super_class/
# -*- coding: utf-8 -*-
#多重継承テスト

class BASE(object):
    def __init__(self):
        print("BASE")
class A(BASE):
    def __init__(self):
        print("A-mae")
        super(A, self).__init__()
        print("A")
class B(BASE):
    def __init__(self):
        print("B-mae")
        super(B, self).__init__()
        print("B")
class MAIN(B, A):

    def __init__(self):
        super(MAIN, self).__init__()
        print("MAIN")

a = MAIN()

