"""
===============================
문제출처  : 백준
문제번호  : max
문제레벨  : 정렬
학습주차  : 프로그래머스
최초생성  : 2022.01.09
생성자    : chung
문제설명  : 정렬
===============================
"""

def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x * 3, reverse=True)
    return str(int(''.join(numbers)))