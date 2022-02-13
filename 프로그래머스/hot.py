import heapq

def solution(sco, k):
    heapq.heapify(sco)
    i = 0
    while sco[0] < k:
        if len(sco) > 1:
            heapq.heappush(sco, heapq.heappop(sco) + (heapq.heappop(sco) * 2))
            i += 1
        else:
            return -1
    return i