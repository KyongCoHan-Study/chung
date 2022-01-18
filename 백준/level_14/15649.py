"""
===============================
문제출처  : 백준
문제번호  : 15649
문제단계  : level_14
최초생성  : 2022.01.18
생성자    : chung
문제설명  : n과m
===============================
"""
def backtrack():
    if len(answer)==M:
        print(" ".join(map(str,answer)))
        return
    for i in range(1,N+1):
        if i not in answer:
            answer.append(i)
            backtrack()
            answer.pop()

N, M = map(int, input().split())

answer=[]
backtrack()