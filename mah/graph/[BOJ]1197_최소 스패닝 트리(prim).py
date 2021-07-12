import sys
import heapq
input = sys.stdin.readline

V, E = map(int, input().split())
graph = {v+1:[] for v in range(V)}

for _ in range(E):
    u, v, w = list(map(int, input().split()))
    graph[u].append([w, u, v])
    graph[v].append([w, v, u])
    

def prim(start):
    mst = []
    weights = 0
    visited = [False] * (V+1)
    visited[start] = True
    num_node = len(graph)
    candis = graph[start]
    heapq.heapify(candis)
    
    while candis and len(mst) < num_node-1:
        w, u, v = heapq.heappop(candis)
        
        if not visited[v]:
            visited[v] = True
            mst.append([u, v])
            weights += w
            
            for n_w, n_v, n_u in graph[v]:
                if visited[n_u]: continue
                heapq.heappush(candis, [n_w, n_v, n_u])
    
    return weights

print(prim(1))