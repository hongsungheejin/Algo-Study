
def dfs(r,c,search_point, direction_check, standard_point):
    global flag
    global visited
    global board
    
    if r == standard_point[0] and c == standard_point[1]:
        #맨 처음일때는 봐줌
        if flag:
            print("Yes")
            exit()
        else:
            flag = True
    
    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]
        
        if nr < 0 or nr >= N or nc < 0 or nc >= M:
            continue
        
        insert_check = []
        for n in range(len(direction_check)):
            insert_check.append(direction_check[n])
        
        insert_check[d] = 1
        
        if board[nr][nc] == search_point and visited[nr][nc] == 0:
            if nr == standard_point[0] and nc == standard_point[1] and sum(insert_check) != 4:
                continue
            visited[nr][nc] = 1
            dfs(nr,nc,search_point,insert_check,standard_point)
        
if __name__ == "__main__":
    N, M = map(int, input().split())
    board = []
    visited = []
    flag = False
    dr = [1,-1,0,0]
    dc = [0,0,1,-1]
    standard_r = 0
    standard_c = 0 
    for _ in range(N):
        board.append(list(input()))
    
    for i in range(N):
        for j in range(M):
            flag = False
            visited = [[0] * M for _ in range(N)]
            dfs(i,j,board[i][j], [0,0,0,0], [i,j])     
            
    print("No")
