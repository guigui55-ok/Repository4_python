import re

def is_match_pattern(pattern:str, value:str):
    ret = re.search(pattern, value)
    if ret!=None:
        return True
    else:
        return False


target = 'abcdefg'
pattern = 'abc'

print()
print('*****')
print(f'target = {target}')
print(f'pattern = {pattern}')
ret = is_match_pattern(pattern, target)
print(ret)