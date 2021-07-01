import sys
import heapq
input = sys.stdin.readline

N = int(input())
lectures = [list(map(int, input().split())) for _ in range(N)]
lectures = sorted(lectures, key=lambda x:x[0])

que = []
heapq.heappush(que, lectures[0][1])

for i in range(1, N):
    if que[0] > lectures[i][0]:
        heapq.heappush(que, lectures[i][1])
    else:
        heapq.heappop(que)
        heapq.heappush(que, lectures[i][1])

print(len(que))