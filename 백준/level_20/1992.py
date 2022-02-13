"""
===============================
문제출처  : ~/Documents/GitHub/chung/백준/level_20
문제번호  : 1992
문제단계  : ~/Documents/GitHub/chung/백준/level_20
최초생성  : 2022.02.13
생성자    : chung
문제설명  : 쿼드트리
===============================
"""
n = int(input())
graph = [list(map(int, input())) for _ in range(n)]


def dnc(x, y, n):
    check = graph[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if check != graph[i][j]:
                check = -1
                break

    if check == -1:
        print("(", end='')
        n = n // 2
        dnc(x, y, n)  
        dnc(x, y + n, n)  
        dnc(x + n, y, n)  
        dnc(x + n, y + n, n)  
        print(")", end='')

    elif check == 1:
        print(1, end='')
    else:
        print(0, end='')


dnc(0, 0, n)
