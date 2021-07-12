N, M = list(map(int, input().split()))
maps = [list(map(int, input().split())) for _ in range(N)]

clouds = [
    [N-2, 0], [N-2, 1],
    [N-1, 0], [N-1, 1],
]

moves = {
    1: [0, -1], 2: [-1, -1], 3: [-1, 0], 4: [-1, 1],
    5: [0, 1], 6: [1, 1], 7: [1, 0], 8: [1, -1]
}

for m in range(M):
    d, s = list(map(int, input().split()))
    
    # 1. 모든 구름이 di 방향으로 si칸 이동한다.    
    move = moves[d]
    dy, dx = move[0] * s, move[1] * s
    clouds = [[(cloud[0]+dy)%N, (cloud[1]+dx)%N] for cloud in clouds]
    # 2. 각 구름에서 비가 내려 구름이 있는 칸의 바구니에 저장된 물의 양이 1 증가한다.
    for cy, cx in clouds:
        maps[cy][cx] += 1
        
    # 3, 4. 2에서 물이 증가한 칸 (r, c)에 물복사버그 마법을 시전한다. 
    # 물복사버그 마법을 사용하면, 대각선 방향으로 거리가 1인 칸에 
    # 물이 있는 바구니의 수만큼 (r, c)에 있는 바구니의 물이 양이 증가한다.
    adds = []
    for cy, cx in clouds:
        count = 0
        for diag_y, diag_x in (cy+1, cx+1), (cy-1, cx-1), (cy+1, cx-1), (cy-1, cx+1):
            if diag_y < 0 or diag_y >= N or diag_x < 0 or diag_x >= N: continue
            if maps[diag_y][diag_x] < 1: continue 
            
            count += 1
        adds.append(count)
    
    old_clouds = set()
    for (cy, cx), add in zip(clouds, adds):
        maps[cy][cx] += add
        old_clouds.add((cy, cx))
    
    # 5. 바구니에 저장된 물의 양이 2 이상인 모든 칸에 구름이 생기고, 물의 양이 2 줄어든다.
    # 이때 구름이 생기는 칸은 3에서 구름이 사라진 칸이 아니어야 한다.
    clouds = []    
    for n in range(N):
        for m in range(N):
            if maps[n][m] >= 2 and (n, m) not in old_clouds:
                maps[n][m] -= 2
                clouds.append([n, m])
    

ans = 0
for row in maps:
    ans += sum(row)
print(ans)