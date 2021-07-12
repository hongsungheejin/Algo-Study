N, K = list(map(int, input().split()))

dp = [[0] * (K+1) for _ in range(N+1)]
dp[0][0] = 1

for i in range(1, N+1):
    for j in range(K+1):
        if i == j or j == 0: dp[i][j] = 1
        elif j > i: break
        else:
            dp[i][j] = (dp[i-1][j] + dp[i-1][j-1])%10_007

print(dp[N][K])