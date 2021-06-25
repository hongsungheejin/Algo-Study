board = []
search_point = []

check_list = [[[0 for i in range(9)] for j in range(3)] for k in range(10)] # 10, 3, 9 -> (1 ~ 10 까지), (행,열,사각형 체크), 9개씩

def search(depth):
    # 끝까지 돌았으면
    if depth == len(search_point):
        for row in board:
            print(*row) # 혼난 부분
        exit()
    
    r, c = search_point[depth]

    for i in range(1,10):
        if check_list[i][0][r] == 0 and check_list[i][1][c] == 0 and check_list[i][2][((r // 3) * 3) + (c // 3)] == 0:
            board[r][c] = i
            check_list[i][0][r] = 1
            check_list[i][1][c] = 1
            check_list[i][2][((r // 3) * 3) + (c // 3)] = 1
            
            search(depth+1)
            
            check_list[i][0][r] = 0
            check_list[i][1][c] = 0
            check_list[i][2][((r // 3) * 3) + (c // 3)] = 0
            board[r][c] = 0
            
        
if __name__ == '__main__':
    board = []
    for _ in range(9):
        insert = list(map(int, input().split()))
        board.append(insert)
    search_point = []
    
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                search_point.append([i,j])
                continue
            check_list[board[i][j]][0][i] = 1
            check_list[board[i][j]][1][j] = 1
            check_list[board[i][j]][2][((i // 3) * 3) + (j // 3)] = 1
    
    search(0)