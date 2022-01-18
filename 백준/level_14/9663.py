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


def N_Queen(board,row):
    global result 
    if row > len(board):
        return
    for i in range(len(board)):
        if can_Move(i,row):
            board[i,row] = 1
            if row==len(board):
                result+=1
            N_Queen(board,row+1)
    return

def can_Move(board,col,row):
    if col < 0 or row < 0: return True
    
    if board[col,row]==1:
        return False
    elif can_Move(board,col-1,row-1)==1:
        return False

result = 0
N=int(input())
board=[[0]*N]*N
N_Queen(board,0)
print(result)