"""
===============================
문제출처  : 프로그래머스
문제번호  : find_prime
문제단계  : 그리디
최초생성  : 2022.01.22
생성자    : chung
문제설명  : 소수 찾기
===============================
"""

import math
from itertools import permutations

def solution(numbers):
    answer = []
    for i in range(1, len(numbers)+1):              
        arr = list(permutations(numbers, i))        
        for j in range(len(arr)):                
            num = int(''.join(map(str,arr[j])))     
            if prime_check(num):                
                answer.append(num)                 
    
    answer = list(set(answer))                      
    return len(answer)
    
def prime_check(n):
    if n <= 1 :
        return False
    for div in range(2,int(math.sqrt(n))+1):
        if n%div == 0:
            return False
    return True

solution("321")