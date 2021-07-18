N, M = list(map(int, input().split()))
size = max(N, M)
if N > M:
    N, M = M, N

dp = [[-1] * (size+1) for _ in range(size+1)]


def solve(n, m):
    global dp

    # (1, 1)을 만들 수 있는 경우 무조건 이김
    if n == 1 and m == 1:
        return 2
    # 메모이제이션
    if dp[n][m] != -1:
        return dp[n][m]
    # 초기값은 B가 이기는 상황
    dp[n][m] = 0
    for i in [n,m]:
      check = solve(1, i-1)
      if check==0 or check==2:
        dp[n][m]=1
        dp[m][n]=1
    return dp[n][m]
solve(N, M)
for i in dp:
  print(i)
print('A' if dp[N][M] == 1 else 'B')
