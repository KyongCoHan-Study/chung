"""
===============================
문제출처  : 백준
문제번호  : 2981
문제단계  : level_17
최초생성  : 2022.02.01
생성자    : chung
문제설명  : 검문
===============================
"""

N=int(input())
M=[int(input()) for _ in range(N)]
M.sort()
result = []
nums = [M[i+1]-M[i] for i in range(N-1)]

for i in range(min(nums),2,-1):
    temp=nums.copy()
    temp=map(lambda x:x%i,temp)
    if sum(temp)==0:
        mnum=i
        break
        
for i in range(2,int(mnum**0.5+1)):
    if mnum%i==0:
        result.append(i)
        result.append(mnum//i)
result.append(mnum)
print(" ".join(map(str,sorted(set(result)))))



'''
시간초과
def tf(lis,n):
    for m in lis:
        if m%n!=0:
            return False
    return True
        
N=int(input())
M=[int(input()) for _ in range(N)]
result=[]
for i in range(int(min(M)**0.5)): 
    for j in range(2,min(M)+1):
        if tf(map(lambda x:x+i ,M),j):
            result.append(j)
print(" ".join(sorted(set(map(str,result)))))
'''