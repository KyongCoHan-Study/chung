"""
===============================
문제출처  : 백준
문제번호  : 9498
문제레벨  : level_2
학습주차  : week_1
최초생성  : 2022.01.04
생성자    : chung
문제설명  : if
===============================
"""

A = int(input())

if A<60:
    print("F")
elif A<70:
    print("D")
elif A<80:
    print("C")
elif A<90:
    print("B")
else:
    print("A")