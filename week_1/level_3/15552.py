"""
===============================
문제출처  : 백준
문제번호  : 15552
문제레벨  : level_3
학습주차  : week_1
최초생성  : 2022.01.05
생성자    : chung
문제설명  : for
===============================
"""
import sys

T = int(sys.stdin.readline())

for i in range(T):
    a, b = map(int, sys.stdin.readline().split())
    print(a+b)