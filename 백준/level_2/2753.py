"""
===============================
문제출처  : 백준
문제번호  : 2753
문제레벨  : level_2
학습주차  : week_1
최초생성  : 2022.01.04
생성자    : chung
문제설명  : if
===============================
"""

A = int(input())

if A%4==0:
    if A%100!=0 or A%400==0:
        print(1)
    else:
        print(0)
else:
    print(0)