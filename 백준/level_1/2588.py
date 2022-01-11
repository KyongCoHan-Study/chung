"""
===============================
문제출처  : 백준
문제번호  : 2588
문제레벨  : level_1
학습주차  : week_1
최초생성  : 2022.01.04
생성자    : chung
문제설명  : multi
===============================
"""
import sys

A = int(sys.stdin.readline())
B = str(sys.stdin.readline())

print(A*int(B[2]))
print(A*int(B[1]))
print(A*int(B[0]))
print(A*int(B))


