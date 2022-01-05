"""
===============================
문제출처  : 백준
문제번호  : 10871
문제레벨  : level_3
학습주차  : week_1
최초생성  : 2022.01.04
생성자    : chung
문제설명  : for
===============================
"""

import sys

N,X = map(int,sys.stdin.readline().split())
n = list(map(int,sys.stdin.readline().split())) 
for i in range(N):
    
    if X>int(n[i]):
        print(n[i],end=" ")
    