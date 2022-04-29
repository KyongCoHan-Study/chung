

def solution(begin, target, words):
    answer = 0
    tran = [0 for _ in range(len(begin))]
    begins= map(chr,list(begin))
    result=[]
    count=0
    
    while True:
        if target in result:
            answer = count
            break
        if count > len(words):
            break
        for word in words:
            cnt = 0
            for a,b in zip(begin,word):
                if a!=b:
                    cnt+=1
            if cnt==1:
                result.append(word)
                count+=1
            
    
    print(result)
    return answer

print(solution("hit",	"cog",	["hot", "dot", "dog", "lot", "log", "cog"]	))