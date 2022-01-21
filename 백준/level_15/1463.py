"""
===============================
문제출처  : 백준
문제번호  : 1463
문제단계  : level_15
최초생성  : 2022.01.21
생성자    : chung
문제설명  : 1로
===============================
"""
N = int(input())
result=[0]*(N+1)
result[1]=0
if N ==1:
    print(0)
else:
    for i in range(1,N):
        if result[i+1]:
            result[i+1]=min(result[i]+1,result[i+1])
        else: result[i+1]=result[i]+1
        if i*2<=N:
            if result[i*2]:
                result[i*2]=min(result[i]+1,result[i*2])
            else: result[i*2]= result[i]+1
        if i*3<=N:
            if result[i*3]:
                result[i*3]=min(result[i]+1,result[i*2])
            else: result[i*3]= result[i]+1
    print(result[N])