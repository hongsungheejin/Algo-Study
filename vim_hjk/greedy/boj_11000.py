import sys
import heapq

input = sys.stdin.readline

N = int(input())

classes = [list(map(int, input().split())) for _ in range(N)]
room = []

classes = sorted(classes, key=lambda x:x[0])

heapq.heappush(room, classes.pop(0)[1])

for start, end in classes:
  if room[0] > start:
    heapq.heappush(room, end)
  else:
    heapq.heappop(room)
    heapq.heappush(room, end)

print(len(room))