"""
===============================
문제출처  : 백준
문제번호  : 1003
문제단계  : level_15
최초생성  : 2022.01.19
생성자    : chung
문제설명  : 피보나치
===============================
"""

import sys

def fibonacci(n):
    if n<3:
        return
    elif result_0[n]==0:
        fibonacci(n-1)
        fibonacci(n-2)
        result_0[n]=result_0[n-1]+result_0[n-2]
        result_1[n]=result_1[n-1]+result_1[n-2]


        
T = int(sys.stdin.readline())
num_0=0
num_1=0
result_0=[0]*41
result_0[0:2]= 1,0,1
result_1=[0]*41
result_1[0:2]= 0,1,1


for _ in range(T):
    n=int(sys.stdin.readline())
    fibonacci(n)
    print(result_0[n],result_1[n])



'''
N = int(input())
one=[0]*41
zero=[0]*41

one[0:2]=[0,1,1]
zero[0:2]=[1,0,1]
for _ in range(N):
    nums=(int(input()))
    
    if nums>2:
        for i in range(2,nums+1):
            if one[i]==0:
                one[i]=one[i-2]+one[i-1]
                zero[i]=zero[i-2]+zero[i-1]
    print(zero[nums],one[nums])
        
        
'''