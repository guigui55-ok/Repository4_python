buf = """
ITスキル	インフラ/運用基盤	-	Active Directory	
-

Amazon Web Services	
-

Apache	
-
"""

from skill_sheet_list_data import SKILL_LIST_BASE
buf = SKILL_LIST_BASE

class CategoryData():
    def __init__(self, cat_title) -> None:
        self.cat_title = cat_title
        self.data_list=[]
    def append_data(self,data):
        self.data_list.append(data)
    def append(self,data):
        self.data_list.append(data)
    def __str__(self) -> str:
        self.cat_title

print()
print('*****')

NEW_LINE = '\n'
# buf = buf.replace(NEW_LINE+'-'+NEW_LINE,'')
buf = buf.replace('\t' + '-', NEW_LINE)
buf = buf.replace('-' + '\t', NEW_LINE)
buf = buf.replace('\t', NEW_LINE)

buf_list = buf.split(NEW_LINE)
buf_list = [s for s in buf_list if s.strip()]
buf_list = [s for s in buf_list if s!='-']
# buf_list = [s for s in buf_list if s!=NEW_LINE]
data_list_all = buf_list
print('buf len = {}'.format(len(data_list_all)))
import pprint
# pprint.pprint(data_list_all[:10])


from skill_sheet_list_data import MIDDLE_CAT_LIST

def is_match_middle_cat_list(data):
    for middle_cat in MIDDLE_CAT_LIST:
        if data == middle_cat:
            return True
    return False

import copy
large_cat_title = 'ITスキル'
large_cat = CategoryData(large_cat_title)
now_mid_cat = CategoryData('')
for i, data in enumerate(data_list_all):
    # if '-' in data:
    if is_match_middle_cat_list(data):
        print('{},  {}'.format(i, data))
        # append before
        large_cat.append(copy.copy(now_mid_cat))
        # create new
        now_mid_cat = CategoryData(data)
        continue
    else:
        now_mid_cat.append(data)

print('large_cat len = {}'.format(len(large_cat.data_list)))
# pprint.pprint(large_cat)

print('=====')
mid_cat:CategoryData = large_cat.data_list[1]
print('mid_cat len = {}'.format(len(mid_cat.data_list)))
pprint.pprint(mid_cat.data_list)
