N = int(input())
one=[0]*41
zero=[0]*41

one[1]=1
zero[0]=1
for _ in range(N):
    nums=(int(input()))
    
    if nums>2:
        for i in range(2,nums+1):
            if one[i]==0:
                one[i]=one[i-2]+one[i-1]
                zero[i]=zero[i-2]+zero[i-1]
    print(zero[nums],one[nums])
        
        