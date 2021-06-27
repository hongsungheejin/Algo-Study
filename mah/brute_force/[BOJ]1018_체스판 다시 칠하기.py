f_boards = [
    [
        "WBWBWBWB", "BWBWBWBW", "WBWBWBWB", "BWBWBWBW",
        "WBWBWBWB", "BWBWBWBW", "WBWBWBWB", "BWBWBWBW",
    ],
    
    [
        "BWBWBWBW", "WBWBWBWB", "BWBWBWBW", "WBWBWBWB", 
        "BWBWBWBW", "WBWBWBWB", "BWBWBWBW","WBWBWBWB",
    ]
]


N, M = map(int, input().split())
board = [str(input()) for _ in range(N)]

ans = float("inf")
for i in range(N-7):
    for j in range(M-7):
        for k in range(2):
            count = 0
            
            for n in range(8):
                for m in range(8):
                    if f_boards[k][n][m] != board[i+n][j+m]: count += 1
            
            ans = min(ans, count)
print(ans)