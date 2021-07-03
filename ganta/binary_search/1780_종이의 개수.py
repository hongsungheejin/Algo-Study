import sys

input = sys.stdin.readline

board = []

check1 = 0
check2 = 0
check3 = 0

def check_square(r,c,n):
    check_num = board[r][c]
    
    for i in range(r, r+n):
        for j in range(c,c+n):
            if check_num != board[i][j]:
                return -2
    return check_num
    
def search(r,c,n):
    global check1
    global check2
    global check3
    
    res = check_square(r,c,n)
    
    if res == -1:
        check1 += 1
        return
    elif res == 0:
        check2 += 1
        return
    elif res == 1:
        check3 += 1
        return
    
    term = n // 3
    nr1 = r + term
    nr2 = r + (term * 2)
    nc1 = c + term
    nc2 = c + (term * 2)
    
    search(r,c,term)
    search(r,nc1,term)
    search(r,nc2,term)
    search(nr1,c,term)
    search(nr1,nc1,term)
    search(nr1,nc2,term)
    search(nr2,c,term)
    search(nr2,nc1,term)
    search(nr2,nc2,term)


if __name__ == "__main__":
    N = int(input())
    
    for _ in range(N):
        board.append(list(map(int,input().split())))
        
    search(0,0,N)
        
    print(check1)
    print(check2)
    print(check3)
    
    