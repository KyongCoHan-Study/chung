"""
===============================
문제출처  : 백준
문제번호  : 2447
문제단계  : level_10
최초생성  : 2022.01.11
생성자    : chung
문제설명  : 별찍기
===============================
"""
def new_pattern(n):
    if n==1:
        return ['*']
    answer = new_pattern(n//3)
    new_answer = [[second for second in first*3] for first in answer*3 ]
    old_length=len(answer)
    for x in range(old_length*3):
        for y in range(old_length*3):
            if old_length<x<=old_length*2 and old_length<y<=old_length*2:
                new_answer[x-1][y-1]=' '
    return new_answer

N=int(input())
for i in new_pattern(N):        
    for j in i:    
        print(j, end='')
    print()

 