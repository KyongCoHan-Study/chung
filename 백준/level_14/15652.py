"""
===============================
문제출처  : 백준
문제번호  : 15652
문제단계  : level_14
최초생성  : 2022.01.18
생성자    : chung
문제설명  : NnM
===============================
"""

def backtrack(n):
    if len(answer)==M:
        print(" ".join(map(str,answer)))
        return
    for i in range(n,N+1):
            answer.append(i)
            backtrack(i)
            answer.pop()

N, M = map(int, input().split())

answer=[]
backtrack(1)