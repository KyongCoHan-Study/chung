"""
===============================
문제출처  : 백준
문제번호  : 5086
문제단계  : level_17
최초생성  : 2022.02.01
생성자    : chung
문제설명  : 배수와 약수
===============================
"""

import sys

while True:
    m,n= map(int,sys.stdin.readline().split())
    if m==n==0:
        break
    if m>n:
        if m%n==0:
            print("multiple")
        else:
            print("neither")
    else:
        if n%m==0:
            print("factor")
        else:
            print("neither")