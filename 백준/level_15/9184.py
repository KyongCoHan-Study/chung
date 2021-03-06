"""
===============================
문제출처  : 백준
문제번호  : 9184
문제단계  : level_15
최초생성  : 2022.01.19
생성자    : chung
문제설명  : 신나는 함수 실행
===============================
"""
import sys
def w(a,b,c):
    if a<=0 or b<=0 or c<=0:
        return 1
    if a>20 or b>20 or c>20:
        return w(20,20,20)
    if wn[a][b][c]:
        return wn[a][b][c]
    if a<b<c:
        wn[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        return wn[a][b][c]
    wn[a][b][c]=w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
    return wn[a][b][c]
wn=[[[0]*21 for _ in range(21)]for _ in range(21)]
while True:
    a, b, c= map(int, sys.stdin.readline().split())
    if a==-1 and b==-1 and c==-1: break
    w(a,b,c)
    print("w({0}, {1}, {2}) = {3}".format(a,b,c,w(a,b,c)))
    
    
'''
def w(a,b,c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)
    if result[a][b][c]:
        return result[a][b][c]
    if a < b< c:
        result[a][b][c]=w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        return result[a][b][c]
    result[a][b][c]=w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
    return result[a][b][c]

result=[[[0]*21 for _ in range(21)]for _ in range(21)]
while True:
    a,b,c=map(int,input().split())
    
    if a==-1 and b==-1 and c==-1:
        break
    print("w({0}, {1}, {2}) = {3}".format(a,b,c,w(a,b,c)))
    '''

