import sys
from collections import deque
from collections import defaultdict
input = sys.stdin.readline


if __name__ == "__main__":
    N, Q = list(map(int, input().split()))
    mootube = [[0] * (N+1) for _ in range(N+1)]
    
    mootube = defaultdict(list)
    for i in range(N-1):
        p, q, r = list(map(int, input().split()))
        mootube[p].append((q, r))
        mootube[q].append((p, r))
    
    INF = float('inf')
    for _ in range(Q):
        dists = [INF] * (N+1)
        visit = [False] * (N+1)
        
        k, start = list(map(int, input().split()))
        dists[start] = 0
        
        que = [start]
        que = deque(que)
        while que:
            cur_node = que.popleft()
            
            if visit[cur_node]: continue
            else:
                visit[cur_node] = True
                
                for next_node, usado in mootube[cur_node]:
                    if visit[next_node]: continue
                    
                    if cur_node != start:
                        dists[next_node] = min(usado, dists[next_node], dists[cur_node])
                    else:
                        dists[next_node] = min(usado, dists[next_node])
                    que.append(next_node)
    
        ans = 0
        for item in dists:
            if item >= k and item != INF: ans += 1
        print(ans)