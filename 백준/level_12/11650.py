"""
===============================
문제출처  : 백준
문제번호  : 11650
문제단계  : level_12
최초생성  : 2022.01.12
생성자    : chung
문제설명  : sort
===============================
"""

import sys

N = int(sys.stdin.readline())
xy=[list(map(int,sys.stdin.readline().split()))for _ in range(N)]
xy.sort(key=lambda x:x[0])
xy.sort(key=lambda x:x[1])

[print(x[0],x[1]) for x in xy]