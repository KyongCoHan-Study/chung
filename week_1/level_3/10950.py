"""
===============================
문제출처  : 백준
문제번호  : 10950
문제레벨  : level_3
학습주차  : week_1
최초생성  : 2022.01.04
생성자    : chung
문제설명  : for
===============================
"""

T = int(input())

for i in range(T):
    A,B = map(int,input().split())
    print(A+B)