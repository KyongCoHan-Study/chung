"""
===============================
문제출처  : 백준
문제번호  : 13305
문제단계  : level_16
최초생성  : 2022.01.21
생성자    : chung
문제설명  : 주유소
===============================
"""

N = int(input())
dis = list(map(int,input().split()))
value = list(map(int,input().split()))
 
result = 0
liter = value[0]
for i in range(len(dis)):
    result = result + dis[i]*liter
    if liter > value[i+1]:
        liter = value[i+1]
print(result)