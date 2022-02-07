"""
===============================
문제출처  : 백준
문제번호  : 1010
문제단계  : level_17
최초생성  : 2022.02.01
생성자    : chung
문제설명  : 다리놓기
===============================
"""

def fac(n):
    result=1
    for i in range(1,n+1):
        result=result*i
    return result

def com(n,m):
    return fac(n)//fac(n-m)//fac(m)

for _ in range(int(input())):
    N,M = map(int,input().split())
    print(com(max(N,M),min(N,M)))