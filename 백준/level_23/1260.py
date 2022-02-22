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
import copy
def dfs(v):
    if v in result_dfs:
        return
    else:
        result_dfs.append(v)
    while tree[v]:
        dfs(tree[v].pop())

def bfs(v):
    if v in result_bfs:
        return
    result_bfs.append(v)
    temp=[]
    while cop[v]:
        bf=cop[v].pop()
        temp.append(bf)
        result_bfs.append(bf)
    temp.reverse()        
    while temp:
        bfs(temp.pop())
        

    

N,M,V = map(int, sys.stdin.readline().split())
tree = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    tree[a].append(b)
    tree[b].append(a)

for i in range(1,N+1):
    tree[i].sort(reverse=True)
cop=copy.deepcopy(tree)
result_dfs=[]
result_bfs=[]

dfs(V)
bfs(V)
print(" ".join(map(str,result_dfs)))

print(" ".join(map(str,result_bfs)))
