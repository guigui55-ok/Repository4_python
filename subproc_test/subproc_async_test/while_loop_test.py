

import time

def main():
    count = 0
    max_sec = 30
    interval = 1
    while True:
        print('{},'.format(count), end='')
        count += 1
        time.sleep(interval)
        if count>=max_sec: break
    return


main()