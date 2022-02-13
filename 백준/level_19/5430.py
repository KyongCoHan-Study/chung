"""
===============================
문제출처  : 백준
문제번호  : 5430
문제단계  : level_19
최초생성  : 2022.02.04
생성자    : chung
문제설명  : ac
===============================
"""

import sys
from collections import deque

for _ in range(int(sys.stdin.readline())):
    AC = sys.stdin.readline().rstrip()
    n = int(sys.stdin.readline())
    arr = sys.stdin.readline().rstrip()[1:-2].split(",")
    queue = deque(arr)

    rev, front, back = 0, 0, len(queue)-1
    flag = 0
    if n == 0:
        queue = []
        front = 0
        back = 0

    for j in AC:
        if j == 'R':
            rev += 1
        elif j == 'D':
            if len(queue) < 1:
                flag = 1
                print("error")
                break
            else:
                if rev % 2 == 0:
                    queue.popleft()
                else:
                    queue.pop()
    if flag == 0:
        if rev % 2 == 0:
            print("[" + ",".join(queue) + "]")
        else:
            queue.reverse()
            print("[" + ",".join(queue) + "]")