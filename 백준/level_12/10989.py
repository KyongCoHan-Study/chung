"""
===============================
문제출처  : 백준
문제번호  : 10989
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
import sys

count=[0]*(10001)
for _ in range(int(sys.stdin.readline())):
    num=int(sys.stdin.readline())
    count[num]+=1
for i in range(10001):
    if count[i]!=0:
        for _ in range(count[i]):
            print(i)