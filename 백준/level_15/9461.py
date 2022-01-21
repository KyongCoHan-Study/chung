"""
===============================
문제출처  : 백준
문제번호  : 9461
문제단계  : level_15
최초생성  : 2022.01.21
생성자    : chung
문제설명  : 파도반
===============================
"""

import sys

def P(n):
    if n <10:
        return result[n]
    elif result[n]:
        return result[n]
    else:
        result[n]=P(n-1)+P(n-5)
        return result[n]

T = int(sys.stdin.readline())
result=[0]*101
result[:10]=[1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
for _ in range(T):
    print(P(int(sys.stdin.readline())-1))