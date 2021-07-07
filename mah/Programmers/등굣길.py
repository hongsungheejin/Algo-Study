def solution(m, n, puddles):
    dp = [[0] * m for _ in range(n)]
    
    for px, py in puddles:
        dp[py-1][px-1] = -1
    
    for i in range(m):
        if dp[0][i] == -1: break
        dp[0][i] = 1
        
    for j in range(n):
        if dp[j][0] == -1: break
        dp[j][0] = 1
    
    for j in range(1, n):
        for i in range(1, m):
            if dp[j][i] == -1: continue
            dp[j][i] = (max(0, dp[j-1][i]) + max(0, dp[j][i-1]))%1_000_000_007
    
    return dp[n-1][m-1] % 1_000_000_007