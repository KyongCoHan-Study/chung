def solution(n, computers):
    answer = 0
    line = [0]*n

    def dfs(a,b):
        for i in range(n):
            if computers[b][i] ==1 and b!=i and line[i]==0:
                line[i]=a
                dfs(a,i)
        
    for i in range(n):
        if line[i]==0:
            answer=answer+1
            dfs(answer,i)
            
    return answer

def solution(numbers, target):
    answer = 0
    n=len(numbers)
    def sum(idx,result):
        if idx==n:
            if result==target:
                nonlocal answer 
                answer+=1
            return
        else:
            sum(idx+1,result+numbers[idx])
            sum(idx+1,result-numbers[idx])
        
                
    sum(0,0)            
    return answer