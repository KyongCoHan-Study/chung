"""
===============================
문제출처  : 백준
문제번호  : 18258
문제단계  : level_19
최초생성  : 2022.02.03
생성자    : chung
문제설명  : que
===============================
"""

import sys
from collections import deque

stack_list=deque()   
for _ in range(int(sys.stdin.readline())):
    n = str((sys.stdin.readline().rstrip()))
    if 'pop' == n:
        if len(stack_list)!=0:
            print(stack_list.popleft()) 
        else: print(-1) 
    elif 'size' == n:
        print(len(stack_list))
    elif 'empty' == n:
        if len(stack_list)!=0:
            print(0) 
        else: print(1)
    elif 'front' == n:
        if len(stack_list)!=0:
            print(stack_list[0]) 
        else: print(-1)
    elif 'back' == n:
        if len(stack_list)!=0:
            print(stack_list[-1]) 
        else: print(-1)
    else:
        n,m=n.split()
        stack_list.append(m)