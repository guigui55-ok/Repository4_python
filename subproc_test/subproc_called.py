
def main():
    print(__file__)
    print(__name__)
    # raise
    import sys
    print("1", file=sys.stdout)
    print("0", file=sys.stderr)
    exit(1)

if __name__ == '__main__': main()
