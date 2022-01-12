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

def hanoi(num, a, b, c):
    if num == 1:
        print(a, c)
    else:
        hanoi(num - 1, a, c, b)
        print(a, c)
        hanoi(num - 1, b, a, c)
        
N = int(input())

num = 1
for _ in range(num-1):
    num = num+1
print(num)
hanoi(num, 1, 2, 3)
'''
아래 있는게 목표지점으로 하나 이동하려면 n-1을 보조기둥으로 n을 목표 기둥으로 n-1을 다시 목표로 반복
hanoi 3 1 2 3
3 1->3
    hanoi 2 1 3 2
        2 1->2
            hanoi 1 1 2 3
                1 1->3
            hanoi 1 3 1 2
                1 3->2
    hanoi 2 2 1 3
        2 2->3
            hanoi 1 2 3 1
            1 2->1
            hanoi 1 1 2 3
            1 1->3
'''
