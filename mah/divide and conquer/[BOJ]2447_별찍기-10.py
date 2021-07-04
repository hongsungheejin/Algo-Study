N = int(input())
board = [[' '] * N for _ in range(N)]

def divide_conquer(x, y, N):
    if N == 3:
        for i in range(3):
            board[x][y+i] = "*"
            if i!=1: board[x+1][y+i] = "*"
            board[x+2][y+i] = "*"
    else:
        for j in range(3):
            for i in range(3):
                if j == 1 and i == 1: continue

                n = N // 3
                divide_conquer(x+(j*n), y+(i*n), n)

divide_conquer(0, 0, N)

for row in board:
    print(''.join(row))