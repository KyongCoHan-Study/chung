result=[]
maps_lenth=0
def solution(maps):
    answer = 0
    maps_lenth = len(maps)
    search(maps,maps_lenth-1,maps_lenth-1,0)
    return answer

def search(maps,m,n,cnt):
    mapn = maps.copy()
    if maps[m][n]==0:
        return 10001
    if m == 0 and n==0:
        return cnt
    if m >= maps_lenth or n>=maps_lenth:
        return 10001
    mapn[m][n]=0
    result.append(search(maps,m,n-1,cnt+1),search(maps,m,n+1,cnt+1),search(maps,m-1,n,cnt+1),search(maps,m+1,n,cnt+1))
    result.sort()
    print(result[0])
    

solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]])