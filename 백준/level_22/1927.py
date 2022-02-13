"""
===============================
문제출처  : ~/Documents/GitHub/chung/백준/level_22
문제번호  : 1927
문제단계  : ~/Documents/GitHub/chung/백준/level_22
최초생성  : 2022.02.13
생성자    : chung
문제설명  : 
===============================
"""

import sys
import heapq

heap = []
n = int(sys.stdin.readline())
for _ in range(n):
  m = int(sys.stdin.readline())
  if m == 0:
    if len(heap) == 0:
      print(0)
    else:
      print(heapq.heappop(heap))
  else:
    heapq.heappush(heap, m)