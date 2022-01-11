"""
===============================
문제출처  : 백준
문제번호  : 1546
문제레벨  : level_5
학습주차  : week_1
최초생성  : 2022.01.07
생성자    : chung
문제설명  : array
===============================
"""
import sys

n = int(input())  
num = list(map(int, input().split()))
max = max(num)

new = []
for score in num :
    new.append(score/max *100)  

print(sum(new)/n)

