"""
===============================
문제출처  : 백준
문제번호  : 10818
문제레벨  : level_5
학습주차  : week_1
최초생성  : 2022.01.07
생성자    : chung
문제설명  : array
===============================
"""
import sys
N = int(sys.stdin.readline())
num=[N]
num = list(map(int,sys.stdin.readline().split()))
min = sys.maxsize
max= -sys.maxsize
for i in range(N):
    if num[i]>max:
        max=num[i]
    if num[i]<min:
        min=num[i]
    
print(min,max)