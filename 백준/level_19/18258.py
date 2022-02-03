"""
===============================
문제출처  : 백준
문제번호  : 18258
문제단계  : level_19
최초생성  : 2022.02.03
생성자    : chung
문제설명  : que
===============================
"""

import sys

N,K = map(int,sys.stdin.readline().split())
result =[]
nums=[str(i) for i in range(1,N+1)]
for i in range(1,N+1):
    result.append(nums.pop((i*K-1)%len(nums)))
    
print('<'+', '.join(result),end='>')