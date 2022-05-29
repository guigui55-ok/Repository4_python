

def main(mode:int=1):
    if mode==1:
        from inherits.inherit_main import InheritMain
        obj = InheritMain()
        obj.excute()
    elif mode==2:
        from inherits.inherit_main_sub_another import InheritMain
        obj = InheritMain()
        obj.excute_another()
    elif mode==3:
        import inherits.inherit_main
        import inherits.inherit_main_sub_other
        from inherits.inherit_main_sub_other import InheritMain
        obj = InheritMain()
        obj.excute()
        obj.excute_other()

def sub():
    mode = 7
    if mode ==1:
        obj = classA()
    # AT2
    # AT3
    # AT2,AT3
    # AT2,AT3,AT4
    # AT4

    # has AT2,AT3


    # AT2のコードはそのままにしたい
    # できれば、reportはAT3のものに
    # platform共通処理はAT2､AT3共通のものにする
    #   共通化できるところはするAT4として実装
    # （AT2,AT3を両方移譲しているもの、reportとdevinfo、pickled_up_は対策が必要）
    # AT3コードにする
    # AT3拡張できるようにする
    #
    

if __name__ == '__main__':
    main(3)



