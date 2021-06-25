empty = []
sudoku = []

hs = [[0]*10 for i in range(9)]
vs = [[0]*10 for i in range(9)]
boxs = [[0]*10 for i in range(9)]

for x in range(9):
    row = list(map(int, input().split()))
    sudoku.append(row)
    for y in range(9):
        if row[y] == 0: empty.append([x, y])
        else:
            hs[x][row[y]] = 1
            vs[y][row[y]] = 1
            boxs[(x//3)*3+(y//3)][row[y]] = 1

def dfs(empty_idx):
    if empty_idx == len(empty):
        for row in sudoku:
            print(*row)
        exit()
    else:
        x, y = empty[empty_idx]
        box = (x//3)*3 + (y//3)
        
        for candi in range(1, 10):
            if hs[x][candi] or vs[y][candi] or boxs[box][candi]: continue
            hs[x][candi] = 1
            vs[y][candi] = 1
            boxs[box][candi] = 1
            
            sudoku[x][y] = candi
            dfs(empty_idx+1)
            sudoku[x][y] = 0
            
            hs[x][candi] = 0
            vs[y][candi] = 0
            boxs[box][candi] = 0

dfs(0)