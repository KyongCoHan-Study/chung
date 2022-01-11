"""
===============================
문제출처  : 백준
문제번호  : 2439
문제레벨  : level_3
학습주차  : week_1
최초생성  : 2022.01.05
생성자    : chung
문제설명  : for
===============================
"""

N = int(input())

for i in range(N):
    for j in range(N-i-1):
        print(" ",end="")
    for j in range(i+1):
        print("*",end="")
    print("")