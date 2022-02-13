"""
===============================
문제출처  : 백준
문제번호  : 1676
문제단계  : level_17
최초생성  : 2022.02.01
생성자    : chung
문제설명  : 0개수
===============================
"""

def fac(n):
    if n==0:
        return 1
    result=1
    for i in range(1,n+1):
        result=result*i
    return result



N= int(input())
cnt=0

for n in reversed(str(fac(N))):
    if n!='0':
        break
    cnt+=1

print(cnt)