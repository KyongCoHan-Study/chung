"""
===============================
문제출처  : 백준
문제번호  : 10952
문제레벨  : level_4
학습주차  : week_1
최초생성  : 2022.01.05
생성자    : chung
문제설명  : while
===============================
"""
import sys
A,B = 1,1
while A>0 or B>0:
    A,B=map(int,sys.stdin.readline().split())
    print(A+B)
