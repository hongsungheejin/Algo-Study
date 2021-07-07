from collections import deque
dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
deq = deque([[n-1, 0], [n-1, 1], [n-2, 0], [n-2, 1]])

for u in range(m):
    c = [[0] * n for _ in range(n)]
    d, s = map(int, input().split())
    d -= 1
    deq_len = len(deq)
    while deq_len:
        x, y = deq.popleft()
        nx = (x + s * dx[d])%n
        ny = (y + s * dy[d])%n
        deq.append([nx, ny])
        deq_len -= 1

    for k in deq:
        x, y = k
        if c[x][y] == 0:
            arr[x][y] += 1
            c[x][y] = 1

    deq = deque([])
    for x in range(n):
        for y in range(n):
            if c[x][y] == 1:
                cnt = 0
                for i in range(1, 8, 2):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < n and 0 <= ny < n:
                        if arr[nx][ny] > 0:
                            cnt += 1
                arr[x][y] += cnt

    for x in range(n):
        for y in range(n):
            if arr[x][y] >= 2:
                if c[x][y] == 0:
                    arr[x][y] -= 2
                    deq.append([x, y])
answer=0
for i in arr:
  answer+=sum(i)
print(answer)