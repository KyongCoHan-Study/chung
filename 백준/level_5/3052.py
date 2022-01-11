"""
===============================
문제출처  : 백준
문제번호  : 3052
문제레벨  : level_5
학습주차  : week_1
최초생성  : 2022.01.07
생성자    : chung
문제설명  : array
===============================
"""
from sys import stdin

n = [0]*10
cnt = [0]*42

for i in range(10):
    n[i]=int(stdin.readline().rstrip())%42

for i in range(42):
    for j in range(10):
        if i == n[j]:
            cnt[i]+=1

print(42-cnt.count(0))