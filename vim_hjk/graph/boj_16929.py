import sys

input = sys.stdin.readline

N, M = map(int, input().split())

board = [[s for s in input().strip()] for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

is_cycle = False

from collections import deque

def bfs(parent_x, parent_y, x, y, symbol):
    global is_cycle

    q = deque()
    q.append([parent_x, parent_y, x, y])

    while q and not is_cycle:
        parent_x, parent_y, x, y = q.popleft()
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            
            if new_x >= N or new_x < 0 or new_y >= M or new_y < 0: continue

            if (visited[new_x][new_y] == 1) and (board[new_x][new_y] == symbol) and (new_x != parent_x) and (new_y != parent_y):
                is_cycle = True
            if (visited[new_x][new_y] == 0) and (board[new_x][new_y] == symbol):
                visited[new_x][new_y] = 1
                q.append([x, y, new_x, new_y])

# def dfs(x, y, start_x, start_y, distance, symbol):
#     global is_cycle
#     for i in range(4):
#         new_x = x + dx[i]
#         new_y = y + dy[i]

#         if is_cycle: return
#         if new_x >= N or new_x < 0 or new_y >= M or new_y < 0: continue

#         if distance >= 4 and start_x == new_x and start_y == new_y:
#             is_cycle = True
#             return
#         if visited[new_x][new_y] == 0 and board[new_x][new_y] == symbol:
#             visited[new_x][new_y] = 1
#             dfs(new_x, new_y, start_x, start_y, distance + 1, symbol)
#             visited[new_x][new_y] = 0
#     return


# for i in range(N):
#     for j in range(M):
#         start_x = i
#         start_y = j
#         visited[start_x][start_y] = 1
#         dfs(i, j, start_x, start_y, 1, board[i][j])
#         if is_cycle: 
#             print('Yes')
#             sys.exit()

# print('No')

for i in range(N):
    for j in range(M):
        start_x = i
        start_y = j
        visited[start_x][start_y] = 1
        bfs(i, j, i, j, board[i][j])
        if is_cycle: 
            print('Yes')
            sys.exit()
print('No')