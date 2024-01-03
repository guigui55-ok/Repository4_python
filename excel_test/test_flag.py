from enum import IntFlag

class Flag(IntFlag):
    FLAG1 = 1 << 0  # 0000000001 in binary
    FLAG2 = 1 << 1  # 0000000010 in binary
    FLAG3 = 1 << 2  # 0000000100 in binary
    FLAG4 = 1 << 3  # 0000001000 in binary
    FLAG5 = 1 << 4  # 0000010000 in binary
    FLAG6 = 1 << 5  # 0000100000 in binary
    FLAG7 = 1 << 6  # 0001000000 in binary
    FLAG8 = 1 << 7  # 0010000000 in binary
    FLAG9 = 1 << 8  # 0100000000 in binary
    FLAG10 = 1 << 9 # 1000000000 in binary

def check_flags(flags):
    for flag in Flag:
        if flags & flag:
            print(f"{flag.name} is set.")

# フラグをテストする
test_flags = Flag.FLAG1 | Flag.FLAG5 | Flag.FLAG10
check_flags(test_flags)