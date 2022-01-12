"""
===============================
문제출처  : 백준
문제번호  : 7568
문제단계  : level_11
최초생성  : 2022.01.12
생성자    : chung
문제설명  : 브루트포스
===============================
"""
import sys

N = int(sys.stdin.readline())
L=[list(map(int,sys.stdin.readline().split())) for _ in range(N)]
answer=[]
for l in L:
    count=1
    for m in L:
        if l[0] < m[0] and l[1] < m[1]:
            count+=1
    print(count,end=" ")

            