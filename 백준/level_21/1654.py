"""
===============================
문제출처  : ~/Documents/GitHub/chung/백준/level_21
문제번호  : 1654
문제단계  : ~/Documents/GitHub/chung/백준/level_21
최초생성  : 2022.02.13
생성자    : chung
문제설명  : 
===============================
"""

from sys import stdin
K, N = map(int,stdin.readline().split())
li = list(map(int,stdin.readlines()))
h, l = sum(li)//N, 1
while l <= h :
    mid = (h+l)//2
    cnt = sum([x//mid for x in li])
    if cnt < N:
        h = mid - 1
    elif cnt >= N:
        l = mid + 1
        ans = mid
print(ans)