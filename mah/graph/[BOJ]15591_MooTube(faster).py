import sys
from collections import deque
from collections import defaultdict
input = sys.stdin.readline


def bfs(start, minimum):
    visited = [False] * (N+1)
    visited[start] = True
    
    que = deque([start])
    cnt = 0
    
    while que:
        cur_node = que.popleft()
        
        for q, r in mootube[cur_node]:
            if not visited[q] and r >= minimum:
                visited[q] = True
                que.append(q)
                cnt += 1
    return cnt


if __name__ == "__main__":
    N, Q = list(map(int, input().split()))
    mootube = [[0] * (N+1) for _ in range(N+1)]
    
    mootube = defaultdict(list)
    for i in range(N-1):
        p, q, r = list(map(int, input().split()))
        mootube[p].append((q, r))
        mootube[q].append((p, r))
    
    for _ in range(Q):
        K, start = list(map(int, input().split()))
        print(bfs(start, K))