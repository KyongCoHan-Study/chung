"""
===============================
문제출처  : 백준
문제번호  : 11399
문제단계  : level_16
최초생성  : 2022.01.21
생성자    : chung
문제설명  : ATM
===============================
"""



N = int(input())
P = list(map(int,input().split()))
sum=0
for i in range(N):
    sum+=P.pop(P.index(min(P)))*(N-i)
print(sum)