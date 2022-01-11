"""
===============================
문제출처  : 백준
문제번호  : 8958
문제단계  : level_5
최초생성  : 2022.01.11
생성자    : chung
문제설명  : array
===============================
"""

import sys

N = int(sys.stdin.readline().rstrip())
for i in range(N):
    sum, count =0,0
    ox = sys.stdin.readline().rstrip()
    for j in ox:
        if j=="O":
            count+=1
            sum+=count
        else:
            count=0
    print(sum)
