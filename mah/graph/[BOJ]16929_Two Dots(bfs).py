from collections import deque

N, M = list(map(int, input().split()))
board = [list(input()) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if visited[i][j]: continue
        
        token = board[i][j]
        visited[i][j] = True
        que = [[i, j, i, j]]
        que = deque(que)
        
        flag = False
        while que and not flag:
            cx, cy, px, py = que.popleft()
            
            for nx, ny in (cx, cy+1), (cx+1, cy), (cx, cy-1), (cx-1, cy):
                if nx < 0 or nx >= N or ny < 0 or ny >= M: continue
                
                condition = (nx != px) and (ny != py)
                if visited[nx][ny] and board[nx][ny] == token and condition:
                    flag = True
                    break
                                
                if not visited[nx][ny] and board[nx][ny] == token:
                    visited[nx][ny] = True
                    que.append([nx, ny, cx, cy])
        
        if flag:
            print("Yes")
            exit()

print("No")