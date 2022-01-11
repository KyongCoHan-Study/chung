"""
===============================
문제출처  : 백준
문제번호  : 4344
문제단계  : level_5
최초생성  : 2022.01.11
생성자    : chung
문제설명  : array
===============================
"""

num = int(input())

for _ in range(num):
    scores = list(map(int, input().split()))
    avg = sum(scores[1:])/scores[0]
    
    cnt = 0
    for i in scores[1:]:
        if i > avg:
            cnt += 1
            
    per = (cnt/scores[0])*100
    print('%.3f' %per + '%')