buf_base = """
2024年7月14日抹消（4頭）
2024年7月13日抹消（8頭）
2024年7月12日抹消（22頭）
2024年7月11日抹消（26頭）
2024年7月10日抹消（34頭）
2024年7月7日抹消（3頭）
2024年7月6日抹消（15頭）
2024年7月5日抹消（27頭）
2024年7月4日抹消（27頭）
2024年7月3日抹消（54頭）
2024年7月2日抹消（3頭）
2024年6月30日抹消（2頭）
2024年6月29日抹消（16頭）
2024年6月28日抹消（24頭）
2024年6月27日抹消（28頭）
2024年6月26日抹消（52頭）
2024年6月25日抹消（6頭）
2024年6月24日抹消（1頭）
2024年6月23日抹消（1頭）
2024年6月22日抹消（10頭）
2024年6月21日抹消（25頭）
2024年6月20日抹消（29頭）
2024年6月19日抹消（48頭）
2024年6月18日抹消（1頭）
2024年6月16日抹消（3頭）
2024年6月15日抹消（8頭）
2024年6月14日抹消（22頭）
2024年6月13日抹消（23頭）
"""

buf_base = """
2024年7月11日登録（122頭）
2024年7月4日登録（142頭）
2024年6月27日登録（138頭）
2024年6月20日登録（103頭）
2024年6月13日登録（96頭）
"""

buf_list = buf_base.split('\n')
ret_list = []
for buf in buf_list:
    l_pos = buf.find('（') + 1
    r_pos = 2
    buf_b = buf[l_pos:-r_pos]
    if buf_b.isdigit():
        ret_list.append(int(buf_b))

print('\n*****')
import pprint
pprint.pprint(ret_list)
sum = sum(ret_list)
print('sum = {}'.format(sum))