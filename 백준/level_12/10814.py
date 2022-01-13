"""
===============================
문제출처  : 백준
문제번호  : 10814
문제단계  : level_12
최초생성  : 2022.01.13
생성자    : chung
문제설명  : 정렬
===============================
"""

import sys

N = int(sys.stdin.readline())
xy=[list(sys.stdin.readline().split())for _ in range(N)]
xy.sort(key=lambda x:int(x[0]))
[print(x[0],x[1]) for x in xy]