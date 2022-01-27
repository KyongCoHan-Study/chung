
    
def solution(name):

    
    
    answer = 0
    new_name=[]
    alpha=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    loc=0
    cnt_left, cnt_right=0, 0
    for n in name:
        for i,e in enumerate(alpha):
            if n==e:
                new_name.append(i)
    answer+=new_name[0]
    while True:
        if sum(new_name)==100*len(new_name):
            break
        minn=100
        tloc = loc
        for i in range(len(1,new_name)):
            if new_name[i] == 100:
                cnt_right+=(i+loc)%len(new_name)
                continue
            cnt_right+=new_name[(i+loc)%len(new_name)]    
        tloc = loc   
         
        for i in range(len(1,new_name)):
            if n == 100:
                cnt_left+=abs(loc-i)
                continue
            cnt_left+=new_name[abs(loc-i)]    
        answer+=min(cnt_right,cnt_left)
        print(answer)
        loc=tloc
        new_name[loc]=0
        
    return answer        


