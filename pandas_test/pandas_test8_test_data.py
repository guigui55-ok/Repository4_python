"""
pandas その他

テストデータ用意
"""

DF_TEST_DATA_COLUMNS = ['ID', 'ItemName', 'Status', 'Enable', 'Amount', 'Date']

data = """
[['001' 'ItemA' 1 '●' 50 Timestamp('2022-09-27 00:00:00')]
 ['002' 'ItemB' 2 '' 20 Timestamp('2021-07-20 00:00:00')]
 ['003' 'ItemC' 3 '' 80 Timestamp('2022-04-30 00:00:00')]
 ['004' 'ItemD' 1 '' 90 Timestamp('2023-11-02 00:00:00')]
 ['005' 'ItemE' 2 '●' 30 Timestamp('2023-01-25 00:00:00')]
 ['006' 'ItemF' 3 '' 20 Timestamp('2021-10-24 00:00:00')]
 ['007' 'ItemG' 1 '' 60 Timestamp('2022-05-13 00:00:00')]
 ['008' 'ItemA' 2 '' 30 Timestamp('2022-03-06 00:00:00')]
 ['009' 'ItemB' 3 '' 70 Timestamp('2023-05-14 00:00:00')]
 ['010' 'ItemC' 1 '●' 0 Timestamp('2022-09-03 00:00:00')]
 ['011' 'ItemD' 2 '' 20 Timestamp('2021-11-19 00:00:00')]
 ['012' 'ItemA' 3 '' 60 Timestamp('2022-10-06 00:00:00')]
 ['013' 'ItemB' 1 '' 0 Timestamp('2022-08-15 00:00:00')]
 ['014' 'ItemC' 2 '' 20 Timestamp('2022-06-30 00:00:00')]
 ['015' 'ItemD' 3 '●' 60 Timestamp('2022-07-19 00:00:00')]]
"""
data = """
[['001' 'ItemA' 1 '●' 50 Timestamp('2022-08-06 00:00:00')]
 ['002' 'ItemB' 2 '' 20 Timestamp('2021-12-07 00:00:00')]
 ['003' 'ItemC' 3 '' 80 Timestamp('2023-02-25 00:00:00')]]
"""

data = """
[['001' 'ItemA' 1 '●' 50 Timestamp('2023-11-04 00:00:00')]
 ['002' 'ItemB' 2 '' 20 Timestamp('2023-11-08 00:00:00')]
 ['003' 'ItemC' 3 '' 80 Timestamp('2023-11-13 00:00:00')]
 ['004' 'ItemD' 1 '' 90 Timestamp('2023-11-19 00:00:00')]
 ['005' 'ItemE' 2 '●' 30 Timestamp('2023-11-26 00:00:00')]
 ['006' 'ItemF' 3 '' 20 Timestamp('2023-12-04 00:00:00')]
 ['007' 'ItemG' 1 '' 60 Timestamp('2023-12-13 00:00:00')]
 ['008' 'ItemA' 2 '' 30 Timestamp('2023-12-23 00:00:00')]
 ['009' 'ItemB' 3 '' 70 Timestamp('2024-01-03 00:00:00')]
 ['010' 'ItemC' 1 '●' 0 Timestamp('2024-01-15 00:00:00')]
 ['011' 'ItemD' 2 '' 20 Timestamp('2024-01-28 00:00:00')]
 ['012' 'ItemA' 3 '' 60 Timestamp('2024-02-11 00:00:00')]
 ['013' 'ItemB' 1 '' 0 Timestamp('2024-02-26 00:00:00')]
 ['014' 'ItemC' 2 '' 20 Timestamp('2024-03-13 00:00:00')]
 ['015' 'ItemD' 3 '●' 60 Timestamp('2024-03-30 00:00:00')]]
"""

data = data.replace("' '", "', '")
data = data.replace(")]", ")],")
data = data.replace("'●'", ",'●',")
data = data.replace("''", ",'',")
data = data.replace("Timestamp(", " ,")
data = data.replace(")]", "]")
import re
lines = data.split('\n')
new_lines = []
for i, line in enumerate(lines):
    # ret = re.search(r"('Item[A-Z]')(\d{2}  ,)", line)
    ret = re.search(r"('Item[A-Z]')", line)
    if ret!=None:
        buf_a = ret.group(1)
        # pos_a = line.find(buf_a)
        # buf_b = ret.group(3)
        # pos_b = line.find(buf_b)
        new_line = line.replace(buf_a, buf_a + ',')
        # new_line = new_line.replace(buf_b, buf_b +',')
        lines[i] = new_line
        new_lines.append(new_line)
import pprint
# pprint.pprint(new_lines)
# data = ''.join([x[1:-2] for x in new_lines])
print('\n'.join(new_lines))

# ['001', 'ItemA', 1 ,'●', 50  ,'2022-09-27 00:00:00']
DF_TEST_DATA = [
    ['001', 'ItemA', 1 ,'●', 50  ,'2022-09-27 00:00:00'],
    ['002', 'ItemB', 2 ,'', 20  ,'2021-07-20 00:00:00'],
    ['003', 'ItemC', 3 ,'', 80  ,'2022-04-30 00:00:00'],
    ['004', 'ItemD', 1 ,'', 90  ,'2023-11-02 00:00:00'],
    ['005', 'ItemE', 2 ,'●', 30  ,'2023-01-25 00:00:00'],
    ['006', 'ItemF', 3 ,'', 20  ,'2021-10-24 00:00:00'],
    ['007', 'ItemG', 1 ,'', 60  ,'2022-05-13 00:00:00'],
    ['008', 'ItemA', 2 ,'', 30  ,'2022-03-06 00:00:00'],
    ['009', 'ItemB', 3 ,'', 70  ,'2023-05-14 00:00:00'],
    ['010', 'ItemC', 1 ,'●', 0  ,'2022-09-03 00:00:00'],
    ['011', 'ItemD', 2 ,'', 20  ,'2021-11-19 00:00:00'],
    ['012', 'ItemA', 3 ,'', 60  ,'2022-10-06 00:00:00'],
    ['013', 'ItemB', 1 ,'', 0  ,'2022-08-15 00:00:00'],
    ['014', 'ItemC', 2 ,'', 20  ,'2022-06-30 00:00:00'],
    ['015', 'ItemD', 3 ,'●', 60  ,'2022-07-19 00:00:00']
 ]

# 日付は23/11月~24/3月
DF_TEST_DATA_B = [['001', 'ItemA', 1 ,'●', 50  ,'2023-11-04 00:00:00'],
 ['002', 'ItemB', 2 ,'', 20  ,'2023-11-08 00:00:00'],
 ['003', 'ItemC', 3 ,'', 80  ,'2023-11-13 00:00:00'],
 ['004', 'ItemD', 1 ,'', 90  ,'2023-11-19 00:00:00'],
 ['005', 'ItemE', 2 ,'●', 30  ,'2023-11-26 00:00:00'],
 ['006', 'ItemF', 3 ,'', 20  ,'2023-12-04 00:00:00'],
 ['007', 'ItemG', 1 ,'', 60  ,'2023-12-13 00:00:00'],
 ['008', 'ItemA', 2 ,'', 30  ,'2023-12-23 00:00:00'],
 ['009', 'ItemB', 3 ,'', 70  ,'2024-01-03 00:00:00'],
 ['010', 'ItemC', 1 ,'●', 0  ,'2024-01-15 00:00:00'],
 ['011', 'ItemD', 2 ,'', 20  ,'2024-01-28 00:00:00'],
 ['012', 'ItemA', 3 ,'', 60  ,'2024-02-11 00:00:00'],
 ['013', 'ItemB', 1 ,'', 0  ,'2024-02-26 00:00:00'],
 ['014', 'ItemC', 2 ,'', 20  ,'2024-03-13 00:00:00'],
 ['015', 'ItemD', 3 ,'●', 60  ,'2024-03-30 00:00:00'],]

