"""
===============================
문제출처  : 프로그래머스
문제번호  : test
문제단계  : 그리디
최초생성  : 2022.01.23
생성자    : chung
문제설명  : 모의고사
===============================
"""

def solution(answers):
    answer = []
    ans_1=[1, 2, 3, 4, 5]*2001
    ans_2=[2, 1, 2, 3, 2, 4, 2, 5]*1260
    ans_3=[3, 3, 1, 1, 2, 2, 4, 4, 5, 5]*1001
    cnt=[0,0,0]
    for i, ans in enumerate(answers):
        if ans_1[i]==ans:
            cnt[0]+=1
        if ans_2[i]==ans:
            cnt[1]+=1
        if ans_3[i]==ans:
            cnt[2]+=1
    for i,j in enumerate(cnt):
        if j == max(cnt):
            answer.append(i+1)
    return answer