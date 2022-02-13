"""
===============================
문제출처  : ~/Documents/GitHub/chung/프로그래머스
문제번호  : pass
문제단계  : ~/Documents/GitHub/chung/프로그래머스
최초생성  : 2022.02.13
생성자    : chung
문제설명  : 
===============================
"""

def solution(n, times):
    answer = 0
    left, right = 1, max(times) * n
    while left <= right:
        mid = (left+ right) // 2
        people = 0
        for time in times:
            people += mid // time
            if people >= n:
                break
        
        if people >= n:
            answer = mid
            right = mid - 1
        elif people < n:
            left = mid + 1
            
    return answer