"""
===============================
문제출처  : 백준
문제번호  : 1932
문제단계  : level_15
최초생성  : 2022.01.21
생성자    : chung
문제설명  : 정수 삼각형
===============================
"""
import sys

N = int(sys.stdin.readline())
triangle = []
for i in range(N):
    triangle.append(list(map(int, sys.stdin.readline().split())))
k = 2
for i in range(1, N):
    for j in range(k):
        if j == 0:
            triangle[i][j] = triangle[i][j] + triangle[i - 1][j]
        elif i == j:
            triangle[i][j] = triangle[i][j] + triangle[i - 1][j - 1]
        else:
            triangle[i][j] = max(triangle[i - 1][j - 1], triangle[i - 1][j]) + triangle[i][j]
    k += 1
print(max(triangle[N - 1]))