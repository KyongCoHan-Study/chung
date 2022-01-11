"""
===============================
문제출처  : 백준
문제번호  : 11729
문제단계  : level_10
최초생성  : 2022.01.11
생성자    : chung
문제설명  : 하노이 탑
===============================
"""


n = int(input())

def hanoi(n, rod1, rod3, rod2):

    if n == 1: 
        print(rod1, rod3)

    else:
        hanoi(n-1, rod1, rod2, rod3)

        print(rod1, rod3)

        hanoi(n-1, rod2, rod3, rod1)

if n==1:
    print(1)
else: print(n**2-2)
hanoi(n, 1, 3, 2)