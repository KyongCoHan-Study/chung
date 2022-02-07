"""
===============================
문제출처  : 백준
문제번호  : 2156
문제단계  : level_15
최초생성  : 2022.02.05
생성자    : chung
문제설명  : 포도주
===============================
"""

import sys


n = int(sys.stdin.readline())
wine=[int(sys.stdin.readline()) for _ in range(n)]
result=[]
wine.append(0)
if n>3:
    result = [wine[0],wine[1]+wine[0],max(wine[0]+wine[1],wine[1]+wine[2],wine[0]+wine[2])]
    for i in range(3,n):
        result.append(max(wine[i-1]+result[i-3]+wine[i],result[i-2]+wine[i],result[i-1]))
    print(result[n-1])
elif n==1:
    print(wine[0])
elif n==2:
    print(wine[0]+wine[1])    
elif n==3:
    print(max(wine[0]+wine[1],wine[1]+wine[2],wine[0]+wine[2]))

    