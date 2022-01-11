"""
===============================
문제출처  : 백준
문제번호  : 2577
문제레벨  : level_5
학습주차  : week_1
최초생성  : 2022.01.07
생성자    : chung
문제설명  : array
===============================
"""

A = int(input())
B = int(input())
C = int(input())
mul = A*B*C
cnt =[0]*10
for i in range(10):
    for num in str(mul):
        if int(num) == i: cnt[i]+=1   

for i in range(10):
    print(cnt[i])