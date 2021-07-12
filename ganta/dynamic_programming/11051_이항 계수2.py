if __name__ == '__main__':
    N , K = map(int, input().split())
    
    dp = [[0] * (N+1) for _ in range(N+1)]
    
    for i in range(1,N+1):
        for j in range(0,N+1):
            if i == j or j == 0:
                dp[i][j] = 1
            else:
                dp[i][j] = ((dp[i-1][j] + dp[i-1][j-1])) % 10007    
    print(dp[N][K])