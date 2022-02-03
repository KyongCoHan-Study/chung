"""
===============================
문제출처  : 백준
문제번호  : 9012
문제단계  : level_18
최초생성  : 2022.02.03
생성자    : chung
문제설명  : 괄호
===============================
"""
import sys


for _ in range(int(sys.stdin.readline())):
    cnt = 0
    for i in str(sys.stdin.readline().rstrip()):
        if cnt<0: 
            break
        if i=='(':
            cnt+=1
        else:
            cnt-=1
    if cnt==0:
        print("YES")
    else:
        print("NO")
            
     