"""
===============================
문제출처  : 백준
문제번호  : 2609
문제단계  : level_17
최초생성  : 2022.02.01
생성자    : chung
문제설명  : 최대공약수와 최소공배수
===============================
"""

m,n = map(int,input().split())
yaksu = 1
for i in range(1,max(m,n)+1):
    if m%i==0 and n%i==0:
        yaksu=i
print(yaksu)
print(int(n*(m/yaksu)))