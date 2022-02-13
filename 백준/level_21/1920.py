"""
===============================
문제출처  : ~/Documents/GitHub/chung/백준/level_21
문제번호  : 1920
문제단계  : ~/Documents/GitHub/chung/백준/level_21
최초생성  : 2022.02.13
생성자    : chung
문제설명  : 
===============================
"""

import sys 

n = sys.stdin.readline()
N = sorted(map(int,sys.stdin.readline().split()))
m = sys.stdin.readline()
M = map(int, sys.stdin.readline().split())

def binary(l, N, start, end):
    if start > end:
        return 0
    m = (start+end)//2
    if l == N[m]:
        return 1
    elif l < N[m]:
        return binary(l, N, start, m-1)
    else:
        return binary(l, N, m+1, end)

for l in M:
    start = 0
    end = len(N)-1
    print(binary(l,N,start,end))