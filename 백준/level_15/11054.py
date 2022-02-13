"""
===============================
문제출처  : 백준
문제번호  : 11054
문제단계  : level_15
최초생성  : 2022.02.07
생성자    : chung
문제설명  : lis
===============================
"""

import sys

A = int(sys.stdin.readline())
array = [map(int,sys.stdin.readline().split())]

result = [1] * (A+1)

for i in range(1, A):
    for j in range(0, i):
        if array[j] < array[i]:
            result[i] = max(result[i], result[j] + 1)

result = max(result)
print(result)