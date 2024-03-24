
import re

def is_match_patterns_any(value , patterns:'list[str]'):
    value = str(value)
    for pattern in patterns:
        if re.search(pattern, value)!=None:
            return True
    else:
        return False
# value = r'F:\\BACKUP\\BKUP_231115\\repos\\'
value = r'F:\\BACKUP\\BKUP_231115\\repos\\.git\\'
# PATTERN = '\\.git\\'
patterns = ['\.git']
patterns = ['$\.git']
patterns = [r'\.git\\\\$']

ret = is_match_patterns_any(value, patterns)
print('ret = {}'.format(ret))