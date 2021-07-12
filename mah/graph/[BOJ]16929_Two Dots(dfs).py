N, M = list(map(int, input().split()))
board = [list(input()) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

ans = False
def dfs(cx, cy, cnt, token, origin):
    for nx, ny in (cx+1, cy), (cx, cy+1), (cx-1, cy), (cx, cy-1):
        if nx < 0 or nx >= N or ny < 0 or ny >= M: continue
        if cnt >= 4 and origin[0]==nx and origin[1]==ny:
            print("Yes")
            exit()
        
        if not visited[nx][ny] and board[nx][ny] == token:
            visited[nx][ny] = True
            dfs(nx, ny, cnt+1, token, origin)
            visited[nx][ny] = False
            

for i in range(N):
    for j in range(M):
        origin = [i, j]
        visited[i][j] = True
        dfs(i, j, 1, board[i][j], origin)

print("No")