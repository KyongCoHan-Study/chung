"""
===============================
문제출처  : 백준
문제번호  : 1904
문제단계  : level_15
최초생성  : 2022.01.19
생성자    : chung
문제설명  : 01타일
===============================
"""

N=int(input())
memo=[0]*N
memo[1:3]=1,2

for i in range(3,N+1):
    memo[i]=(memo[i-2]+memo[i-1])%15746

if N<3:
    print(memo[N])
else:
    print(memo[N])
