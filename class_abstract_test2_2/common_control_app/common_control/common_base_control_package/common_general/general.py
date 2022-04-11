
bar = '################################################################################'

def print_alert(value):
    print()
    print(bar)
    print('    ' + str(value))
    print(bar)
    print()

def notice_not_implemented():
    print_alert('not implemented')