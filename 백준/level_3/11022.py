"""
===============================
문제출처  : 백준
문제번호  : 11022
문제레벨  : level_3
학습주차  : week_1
최초생성  : 2022.01.05
생성자    : chung
문제설명  : for
===============================
"""

import sys

T = int(sys.stdin.readline())

for i in range(1,T+1):
    a, b = map(int, sys.stdin.readline().split())
    print("Case #"+str(i)+":",a,"+",b,"=",a+b)