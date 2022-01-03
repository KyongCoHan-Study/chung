"""
===============================
문제출처  : 백준
문제번호  : 10430
문제레벨  : level1
학습주차  : week1
최초생성  : 2022.01.04
생성자    : chung
문제설명  : remain
===============================
"""

A,B,C = map(int,input().split())
print((A+B)%C)
print(((A%C)+(B%C))%C)
print((A*B)%C)
print(((A%C)*(B%C))%C)
