import sys
input = sys.stdin.readline

V, E = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(E)]

parents = [-1] * (V+1)
for i in range(1, V+1):
    parents[i] = i

def find_p(parents, node):
    if parents[node] != node:
        parents[node] = find_p(parents, parents[node])
    
    return parents[node]

def union(parents, node_x, node_y):
    node_x = find_p(parents, node_x)
    node_y = find_p(parents, node_y)
    
    if node_x < node_y:
        parents[node_y] = node_x
    else:
        parents[node_x] = node_y
        
edges.sort(key=lambda edge: edge[-1])
weights = 0
for u, v, w in edges:
    if find_p(parents, u) != find_p(parents, v):
        union(parents, u, v)
        weights += w

print(parents)
print(weights)