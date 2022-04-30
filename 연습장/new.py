def solution(compressed):
    answer = ''
    intstack = []
    strstack = []
    temp=''
    for i in range(len(compressed)):
        cnt = 0

        if compressed[i]>='0' and compressed[i]<='9':
            while compressed[i]>='0' and compressed[i]<='9':
                cnt = cnt*10 + int(compressed[i])
                i+=1
            i-=1
            intstack.append(cnt)
            print(intstack)
        elif compressed[i] =='(':
            if compressed[i-1] >='0' and compressed[i-1]<='9':
                strstack.append(compressed[i])
            else:
                strstack.append(compressed[i])
                intstack.append(1)
        elif compressed[i]==')':
            temp=''
            cnt=0
            if intstack:
                cnt=intstack.pop()
            while strstack and strstack[-1] !='(':
                temp = strstack.pop()+temp
            if strstack and strstack[-1] =='(':
                strstack.pop()
            for j in range(cnt):
                answer = answer + temp
            for j in range(len(answer)):
                strstack.append(answer[j])
            answer="";
        else:
            strstack.append(compressed[i])
    while strstack:
        answer = strstack.pop() + answer
        

    return answer

print(solution("10(p)"))