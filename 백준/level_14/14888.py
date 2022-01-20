"""
===============================
문제출처  : 백준
문제번호  : 14888
문제단계  : level_14
최초생성  : 2022.01.19
생성자    : chung
문제설명  : 연산자 넣기
===============================
"""

import sys

def calculate(depth,result,c):
    global maxnum, minnum
    if depth==N:
        maxnum= max(result,maxnum)
        minnum= min(result,minnum)
        return
    for i in range(4):
        if i==0 and c[i]>0:
            copyc=c.copy()
            copyc[i]-=1
            calculate(depth+1,result+num[depth],copyc)
        if i==1 and c[i]>0:
            copyc=c.copy()
            copyc[i]-=1
            calculate(depth+1,result-num[depth],copyc)
        if i==2 and c[i]>0:
            copyc=c.copy()
            copyc[i]-=1
            calculate(depth+1,result*num[depth],copyc)
        if i==3 and c[i]>0:
            copyc=c.copy()
            copyc[i]-=1
            calculate(depth+1,int(result/num[depth]),copyc)

maxnum, minnum=-sys.maxsize, sys.maxsize
N=int(sys.stdin.readline())
num=list(map(int,sys.stdin.readline().split()))
cal=list(map(int,sys.stdin.readline().split()))
calculate(1,num[0],cal)
print(maxnum) 
print(minnum)