"""
===============================
문제출처  : 백준
문제번호  : 9663
문제단계  : level_14
최초생성  : 2022.01.18
생성자    : chung
문제설명  : NQueen
===============================
"""

result = 0
N=int(input())
board=[0]*N

def search(row):
    for i in range(row):
        if abs(board[row]-board[i])==row-i or board[row]==board[i]:
            return False
    return True

def N_Queen(row):
    global result 
    if row == N:
        result+=1
    else:
        for i in range(N):
            board[row]=i
            if search(row):
                N_Queen(row+1)


N_Queen(0)
print(result)



