import sys
import heapq
input = sys.stdin.readline

N, M = list(map(int, input().split()))
companies = [int(input()) for _ in range(N)]

connections = {
    i:{} for i in range(N)
}

for i in range(N):
    row = list(map(int, input().split()))
    for j in range(N):
        if i == j: continue
        if row[j] != 0: 
            connections[i][j] = row[j]
            connections[j][i] = row[j]


dists = {i: [float('inf')]*2 for i in range(N)}
dists[0] = [0, 0]
que = []


heapq.heappush(que, [0, dists[0][1], 0])
while que:
    changes, cur_dist, cur_dest = heapq.heappop(que)
    
    if dists[cur_dest][0] < changes:
        continue
        
    for new_dest, new_dist in connections[cur_dest].items():
        dist = cur_dist + new_dist
        new_changes = changes if companies[new_dest] == companies[cur_dest] else changes + 1
        
        if new_changes <= dists[new_dest][0] and dist < dists[new_dest][1]:
            dists[new_dest][1] = dist
            dists[new_dest][0] = new_changes
            heapq.heappush(que, [new_changes, dist, new_dest])
            
print(*dists[M])