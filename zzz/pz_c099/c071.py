m=11
n=20

match_count = 0
import numpy
for i in range(1,m):
    for j in range(1,n):
        k_squared = abs((i*i)+(j*j))
        k:float = numpy.sqrt(k_squared)
        
        if k > 0:
            if k.is_integer():
                match_count += 1

print(match_count)

# def get_angle_from_sides(a, b, c):
#     """3辺の長さからそれぞれの角度を求める"""
#     return math.acos((a ** 2 + b ** 2 - c ** 2) / (2 * a * b))

# match_count = 0
# import numpy
# import math
# for i in range(1,m):
#     flag = False
#     for j in range(1,n):
#         other_edge_squared = abs((i*i)-(j*j))
#         k:float = numpy.sqrt(other_edge_squared)
#         if k > 0:
#             if k.is_integer():
#                 if (i<k)or(j<k):
#                     # print(other_edge_length)
#                     print('{} , {} = {}'.format(i,j,k))
#                     flag = True
        
#         if not flag:
#             other_edge_squared = abs((i*i)+(j*j))
#             k:float = numpy.sqrt(other_edge_squared)
#             if k > 0:
#                 if k.is_integer():
#                     if (i<k)or(j<k):
#                         # print(other_edge_length)
#                         print('{} , {} = {}'.format(i,j,int(k)))
#                         flag = True
#         if flag:
#             match_count += 1

# print(match_count)