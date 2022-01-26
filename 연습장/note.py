
    
def solution(name):

    
    
    answer = 0
    new_name=[]
    alpha=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    loc=0
    spell=0
    for n in name:
        for i,e in enumerate(alpha):
            if n==e:
                new_name.append(i)
    while True:
        if sum(new_name)==100*len(new_name):
            break
        minn=100
        tspell=spell
        tloc = loc
        for i,n in enumerate(new_name):
            if n == 100:
                continue
            if minn > abs(min(loc-i,i-len(new_name)+loc)+min(abs(n),abs(24-n))):
                        minn = abs(min(abs(loc-i),abs(i-len(new_name)+loc)))+min(abs(n),abs(24-n))
                        tloc=i
                        tspell=n
        answer+=minn
        print(answer)
        loc=tloc
        spell=tspell
        new_name[loc]=100
        
    return answer
JAAAAAJAAAAAAAAAAAAJ 
print(solution("JEROEN"))