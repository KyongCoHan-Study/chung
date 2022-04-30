def solution(n, edge):
    answer = 0
    num = 1
    q=[[1]*n]

    num=0
    while True:
        num+=1
        for i in range(n):
            if  edge[i][0] in q[num-1] and edge[i][1] not in q:
                q[num].append([edge[i][1]])
            elif edge[i][1] in q[num-1] and edge[i][0] not in q:
                q[num].append([edge[i][0]])
        print(q)
        
        if len(q)==n:
            break
    
    
    return len(q)
print(solution(6,	[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))