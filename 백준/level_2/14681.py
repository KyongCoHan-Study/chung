"""
===============================
문제출처  : 백준
문제번호  : 14681
문제레벨  : level_2
학습주차  : week_1
최초생성  : 2022.01.04
생성자    : chung
문제설명  : if
===============================
"""
A=int(input())
B=int(input())

if(A>0):
    if(B>0):
        print(1)
    else:
        print(4)
else:
    if(B>0):
        print(2)
    else:
        print(3)