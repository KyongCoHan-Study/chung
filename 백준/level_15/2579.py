"""
===============================
문제출처  : 백준
문제번호  : 2579
문제단계  : level_15
최초생성  : 2022.01.21
생성자    : chung
문제설명  : 계단 오르기
===============================
"""


import sys

N = int(sys.stdin.readline())
stair = [int(sys.stdin.readline()) for _ in range(N)]
result=[0]*302
if N<3:
    print(sum(stair))
else:
    result[0]=stair[0]
    result[1]=stair[0]+stair[1]
    result[2]=stair[2]+max(stair[1],stair[0])
    for i in range(3,N):
        result[i]=max(result[i-3]+stair[i-1],result[i-2])+stair[i]
    print(result[N-1])