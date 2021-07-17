if __name__ == '__main__':
    n,m = map(int, input().split())
    board = []
    for _ in range(n):
        board.append(list(map(int,list(input()))))
        
    dp = [[0] * m for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            if m == 0 and board[i][j] == 1:
                dp[i][j] = 1
                continue
            if n == 0 and board[i][j] == 1:
                dp[i][j] = 1
                continue
            
            if board[i][j] == 1:
                dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
    
    res = -1
    for d in dp:
        temp = max(d)
        res = max(res, temp)
    print(res**2)
                
            