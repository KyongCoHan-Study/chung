"""
===============================
문제출처  : 백준
문제번호  : 2156
문제단계  : level_15
최초생성  : 2022.02.05
생성자    : chung
문제설명  : 포도주
===============================
"""

import sys

n = int(sys.stdin.readline())
wine=[int(sys.stdin.readline()) for _ in range(n)]
result = []
for i in range(n):
    