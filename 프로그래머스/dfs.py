def solution(n, computers):
    answer = 0
    line = [0]*n

    def dfs(a,b):
        for i in range(n):
            if computers[b][i] ==1 and b!=i:
                line[i]=a
                dfs(a,i)

    for i in range(n):
        if line[i]==0:
            answer=answer+1
            dfs(answer,i)
            
    return answer

solution(3,	[[1, 1, 0], [1, 1, 0], [0, 0, 1]])