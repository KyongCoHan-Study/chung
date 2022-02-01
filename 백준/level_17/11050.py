"""
===============================
문제출처  : 백준
문제번호  : 11050
문제단계  : level_17
최초생성  : 2022.02.01
생성자    : chung
문제설명  : 이항 계수1
===============================
"""
def fac(n):
    result=1
    for i in range(1,n+1):
        result=result*i
    return result
N,K = map(int,input().split())

print(fac(N)//fac(N-K)//fac(K))
