"""
===============================
문제출처  : 프로그래머스
문제번호  : k_num
문제레벨  : 정렬
학습주차  : 프로그래머스
최초생성  : 2022.01.09
생성자    : chung
문제설명  : 
===============================
"""

def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        answer.append(sorted(list(array[int(commands[i][0])-1:int(commands[i][1])]))[commands[i][2]-1])
    return answer