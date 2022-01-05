"""
===============================
문제출처  : 백준
문제번호  : 1110
문제레벨  : level_4
학습주차  : week_1
최초생성  : 2022.01.06
생성자    : chung
문제설명  : while
===============================
"""

N = int(input())  
num = N           
count = 0        
 
while True:
    a = num//10
    b = num %10
    c = (a+b)%10
    num = (b*10) + c
    count += 1
    if(num == N):
        break
 
print(count)