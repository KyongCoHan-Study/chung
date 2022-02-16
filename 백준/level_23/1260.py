"""
===============================
문제출처  : ~/Documents/GitHub/chung/백준/level_23
문제번호  : 1260
문제단계  : ~/Documents/GitHub/chung/백준/level_23
최초생성  : 2022.02.16
생성자    : chung
문제설명  : dfs, bfs
===============================
"""

import sys

def dfs(v):
    result_dfs.append(v)
    if list[v]==0:
        return
    for n in list[v]:
        dfs(n)


N,M,V = map(int, sys.stdin.readline().split())
tree = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    tree[a].append(b)
    tree[b].append(a)

for i in range(1,N+1):
    tree[i].sort(reverse=True)
result_dfs=[]
result_bfs=[]
