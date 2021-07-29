board = []
res  = ""


def check_square(r,c,n):
    global board
    
    check_num = board[r][c]
    
    for i in range(r, r+n):
        for j in range(c, c+n):
            if board[i][j] != check_num:
                return 2
    
    return check_num


def search(r,c,n):
    global res
    
    check_num = check_square(r,c,n)
    
    if check_num == 1:
        res += str(check_num)
    elif check_num == 0:
        res += str(check_num)
    else:
        nr = r + n // 2
        nc = c + n // 2
        res += "("
        search(r,c,n//2)
        search(r,nc,n//2)
        search(nr,c,n//2)
        search(nr,nc,n//2)
        res += ")"

if __name__ == '__main__':
    N = int(input())
    board = []
    
    for _ in range(N):
        board.append(list(map(int,list(input()))))
    
    
    search(0,0,N)
    
    print(res)
    
    