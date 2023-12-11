


start_number = 0
loop_max_count = 100
a_0 = []
a_1 = []
a_2 = []

def save_and_print_remainder(number, loop_max_count):
    number = 1
    for _ in range(loop_max_count):
        remainder = number % 3
        if remainder == 0:
            a_0.append(number)
        elif remainder == 1:
            a_1.append(number)
        elif remainder == 2:
            a_2.append(number)
        number += 1

def print_result():
    print()
    print('### result a_0 ###')
    print(a_0)
    print()
    print('### result a_1 ###')
    print(a_1)
    print()
    print('### result a_2 ###')
    print(a_2)
    print()

def main2():
    save_and_print_remainder(start_number, loop_max_count)
    print_result()

def main():
    n = 1
    max = 100
    for i in range(3):
        buf = [n for n in range(max) if n % 3 == i]
        print()
        print(buf)

if __name__ == '__main__':
    main()