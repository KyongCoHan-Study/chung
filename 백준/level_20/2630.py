"""
===============================
문제출처  : ~/Documents/GitHub/chung/백준/level_20
문제번호  : 2630
문제단계  : ~/Documents/GitHub/chung/백준/level_20
최초생성  : 2022.02.13
생성자    : chung
문제설명  : 색종이
===============================
"""

import sys



N = int(sys.stdin.readline())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)] 
wht=0
blk=0

def cutting(x, y, N) :
  global wht, blk
  color = paper[x][y]
  for i in range(x, x+N) :
    for j in range(y, y+N) :
      if color != paper[i][j] :
        cutting(x, y, N//2)
        cutting(x, y+N//2, N//2)
        cutting(x+N//2, y, N//2)
        cutting(x+N//2, y+N//2, N//2)
        return
  if color == 0 :
    wht+=1
  else :
    blk+=1

cutting(0,0,N)
print(wht)
print(blk)