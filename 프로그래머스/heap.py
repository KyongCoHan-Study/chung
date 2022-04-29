import heapq


def solution(jobs):
    answer = 0
    heap=[]
    time =0
    q=[]
    
    while jobs:
        for i,val in enumerate(jobs):
            if val[0]<=time:
                start,end=val
                heap.append([end,start])
        if heap: 
            print(heap)
            end, start =sorted(heap,key=lambda x:x[0]+time-x[1])[0]
            
            q.append(end+time-start)
            time=time+end
            heap.clear()
        else:
            time+=1
        if len(q)==len(jobs):
            break
    print(q)
    for i in q:
        answer+=i
    return answer/len(q)

print(solution([[0, 3], [1, 9], [2, 6]]))
# def solution(v):
#     answer = [0,0]
    
#     for i in v:
#         tf = [True,True]
#         for j in v:
#             if j[0]==i[0]:
#                 tf[0] = False
#             elif j[1]==i[1]:
#                 tf[1] = False
#         print(tf)
#         if tf[0]:
#             answer[0]=i[0]
#         elif tf[1]:
#             answer[1]=i[1]

#     return answer

# print(solution([[1, 4], [3, 4], [3, 10]]))