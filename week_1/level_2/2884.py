"""
===============================
문제출처  : 백준
문제번호  : 2884
문제레벨  : level_2
학습주차  : week_1
최초생성  : 2022.01.04
생성자    : chung
문제설명  : if
===============================
"""

A,B = map(int,input().split())
time=A*60+B-45
if time<0:
    time=time+24*60
print(str(time//60),str(time%60))