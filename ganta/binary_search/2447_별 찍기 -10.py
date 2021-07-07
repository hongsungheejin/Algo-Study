board = []
standard = [["*", "*", "*"], ["*" , " ", "*"], ["*", "*", "*"]]

def draw(r,c, shape):
    global board
    
    for i in range(r, r + len(shape)):
        for j in range(c, c+ len(shape)):
            board[i][j] = shape[i-r][j-c]

def sketch(r,c,n):
    
    global board
    
    if n == 3:
        draw(r,c,standard)
        return

    term = n // 3
    nr1 = r + term
    nr2 = r + (term * 2)
    nc1 = c + term
    nc2 = c + (term * 2)
    sketch(r,c,n//3)
    sketch(r,nc1, n//3)
    sketch(r,nc2,n//3)
    sketch(nr1,c,n//3)
    sketch(nr1,nc2,n//3)
    sketch(nr2,c,n//3)
    sketch(nr2,nc1,n//3)
    sketch(nr2,nc2,n//3)
    
    return 
    
            
if __name__ == '__main__':
    N = int(input()) 
    board = [[' '] * N for _ in range(N)]
    
    sketch(0,0,N)
    
    for row in board:
        print("".join(row))
    
    