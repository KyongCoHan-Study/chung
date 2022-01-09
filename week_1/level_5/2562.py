"""
===============================
문제출처  : 백준
문제번호  : 2562
문제레벨  : level_5
학습주차  : week_1
최초생성  : 2022.01.07
생성자    : chung
문제설명  : 배열
===============================
"""
import sys

max = - sys.maxsize
cnt=0

for i in range(9):
    N= int(sys.stdin.readline())
    if N > max: 
        max=N
        cnt=i
    
print(max) 
print(cnt+1)
