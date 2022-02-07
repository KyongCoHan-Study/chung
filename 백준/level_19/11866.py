"""
===============================
문제출처  : 백준
문제번호  : 11866
문제단계  : level_19
최초생성  : 2022.02.03
생성자    : chung
문제설명  : 요세푸스 문제 0
===============================
"""

from collections import deque
import sys

N,K = map(int,sys.stdin.readline().split())
nums = deque()
[nums.append(str(i)) for i in range(1,N+1)]
result = []
while nums:
    for i in range(K-1):
        nums.append(nums.popleft())
    result.append(nums.popleft())
    
print('<'+', '.join(result),end='>')