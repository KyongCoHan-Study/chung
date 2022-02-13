"""
===============================
문제출처  : 백준
문제번호  : 10844
문제단계  : level_15
최초생성  : 2022.02.04
생성자    : chung
문제설명  : 계단수
===============================
"""


n = int(input())
dp = [[0 for i in range(10)] for j in range(101)]
dp[1]=[0,1,1,1,1,1,1,1,1,1]
for i in range(2, n + 1):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i - 1][1]
        elif j == 9:
            dp[i][j] = dp[i - 1][8]
        else:
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1]
print(sum(dp[n]) % 1000000000)