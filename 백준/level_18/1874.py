"""
===============================
문제출처  : 백준
문제번호  : 1874
문제단계  : level_18
최초생성  : 2022.02.03
생성자    : chung
문제설명  : 스택수열
===============================
"""

import sys

stack_list=[]  
result=[]
max=0
n=int(sys.stdin.readline())
for i in range(1,n+1):
    
    m = int(sys.stdin.readline())
    if m < max:
        if stack_list[-1]==m:
            stack_list.pop()
            result.append("-")
        else:
            result=["NO"]
            break
    else:
        for j in range(max+1,m+1):
            result.append("+")
            stack_list.append(j)
        stack_list.pop()
        result.append("-")
    if m > max:
        max=m
[print(i) for i in result]