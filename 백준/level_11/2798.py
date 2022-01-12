"""
===============================
문제출처  : 백준
문제번호  : 2798
문제단계  : level_11
최초생성  : 2022.01.12
생성자    : chung
문제설명  : 브루트 포스
===============================
"""

import sys

N,M = map(int,sys.stdin.readline().split())
L=list(map(int,sys.stdin.readline().split()))
answer=0
for m in L:
    for n in L:
        if m==n: continue
        for o in L:
            if n==o: continue
            sum=m+n+o
            if sum>M: continue
            if answer<sum: answer=sum
    L.remove(m)

print(answer)