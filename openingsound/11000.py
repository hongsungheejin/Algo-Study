import sys
import heapq
input = sys.stdin.readline

n = int(input())
l = []
heap = []
l = [list(map(int, input().split())) for _ in range(n)]

l.sort(key=lambda x: (x[0]))

answer = 0
for a, b in l:
    while heap and heap[0] <= a:
        heapq.heappop(heap)
    if(answer - len(heap) == 0):
        answer += 1
    heapq.heappush(heap, b)

print(answer)
