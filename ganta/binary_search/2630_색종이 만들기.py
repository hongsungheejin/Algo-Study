cnt_white = 0
cnt_blue = 0
board = []


def check_square(r,c,n):
    check_num = board[r][c]
    
    for i in range(r, r + n):
        for j in range(c, c + n):
            if check_num != board[i][j]:
                    return -1
    return check_num
    
def func(r,c,n):
    
    global cnt_white
    global cnt_blue
    
    check_num = check_square(r,c,n)
    
    if check_num  == -1:
        nr = (r + (n // 2))
        nc = (c + (n // 2))
        
        func(r, c, n // 2)
        func(nr, c, n // 2)
        func(r, nc, n // 2)
        func(nr, nc, n // 2)
    else: 
        if check_num == 0:
            cnt_white += 1
        else:
            cnt_blue += 1
    
if __name__ == '__main__':
    N = int(input())
    for _ in range(N):
        board.append(list(map(int, input().split())))
    
    
    func(0,0,N)
    print(cnt_white)
    print(cnt_blue)