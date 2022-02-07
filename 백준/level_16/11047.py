"""
===============================
문제출처  : 백준
문제번호  : 11047
문제단계  : level_16
최초생성  : 2022.01.21
생성자    : chung
문제설명  : 동전0
===============================
"""
import sys

N,K=map(int,sys.stdin.readline().split())
cash=[int(sys.stdin.readline()) for _ in range(N)]
cnt=0
cash.reverse()
for n in cash:
    while K>= n:
        cnt+=1
        K=K-n
    if K==0:
        break
print(cnt)