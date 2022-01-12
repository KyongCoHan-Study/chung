"""
===============================
문제출처  : 백준
문제번호  : 2750
문제단계  : level_12
최초생성  : 2022.01.12
생성자    : chung
문제설명  : 정렬
===============================
"""

import sys

##EASY WAY
##[print(n) for n in sorted([int(sys.stdin.readline()) for _ in range(int(sys.stdin.readline()))])]
          
          
##HARD WAY     
N = int(sys.stdin.readline())
num=[int(sys.stdin.readline()) for _ in range(N)]

for i in range(N):
    for j in range(1,N-i):
        if num[j-1] > num[j]:
            temp=num[j-1]
            num[j-1]=num[j]
            num[j]=temp
[print(n) for n in num]