import itertools


def main():
    data = 'ABCD'
    data = 'AA','BB','CC','DD'
    data = 'JAPAN','USA','ITALY','UK'
    for buf in itertools.permutations(data, 2):
        print(buf)


if __name__ == '__main__':
    main()
