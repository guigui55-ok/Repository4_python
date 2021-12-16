
def main():
    try:
        print(__file__)
        print(__name__)
        # raise
        import sys
        print("1", file=sys.stdout)
        print("1", file=sys.stderr)
        # exit(1)
        # sys.stdout= 'success'
        value = 'stdout.write'
        sys.stdout.write(value)
        # 終了ステータスを返す
        ret = [1,'success']
        ret = 1,'success'
        ret = 'success'
        ret = 0
        
        #sys.exit(ret)
        value = 'stderr.wrie'
        sys.stderr.write(value)
        ex = SystemExit(ret)
        ex.code = 2
        ex.args = '3' # TypeError: 'int' object is not iterable
        sys.exit(ex)
        return 1
    except:
        import traceback
        traceback.print_exc()

if __name__ == '__main__': main()
