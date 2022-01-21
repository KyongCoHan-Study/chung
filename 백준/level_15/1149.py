"""
===============================
문제출처  : 백준
문제번호  : 1149
문제단계  : level_15
최초생성  : 2022.01.21
생성자    : chung
문제설명  : rgb거리
===============================
"""

import sys



N = int(sys.stdin.readline())
rgb_list=[]
for i in range(N):
    R,G,B = map(int, sys.stdin.readline().split())
    rgb_list.append([R,G,B])

for i in range(N):
    rgb_list[i][0] = min(rgb_list[i - 1][1], rgb_list[i - 1][2]) + rgb_list[i][0]
    rgb_list[i][1] = min(rgb_list[i - 1][0], rgb_list[i - 1][2]) + rgb_list[i][1]
    rgb_list[i][2] = min(rgb_list[i - 1][0], rgb_list[i - 1][1]) + rgb_list[i][2]    
print(min(rgb_list[N - 1][0], rgb_list[N - 1][1], rgb_list[N - 1][2]))