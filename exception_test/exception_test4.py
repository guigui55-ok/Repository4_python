#https://blog.serverworks.co.jp/2020/09/23/115853


def target():
    try:
        # i=[]
        # i[0]
        1/0  # ZeroDivisionError が起きる
    except IndexError:
        raise IndexError()
        pass
    except Exception as err:
        raise Exception("IndexError 以外の何かしらのエラーが発生しました") from err

if __name__ == '__main__':
    target()