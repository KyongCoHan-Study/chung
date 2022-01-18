"""
===============================
문제출처  : 백준
문제번호  : 15651
문제단계  : level_14
최초생성  : 2022.01.18
생성자    : chung
문제설명  : NnM
===============================
"""

def backtrack():
    if len(answer)==M:
        print(" ".join(map(str,answer)))
        return
    for i in range(1,N+1):

            answer.append(i)
            backtrack()
            answer.pop()

N, M = map(int, input().split())

answer=[]
backtrack()