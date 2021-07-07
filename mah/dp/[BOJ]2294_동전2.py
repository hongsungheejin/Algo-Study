import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = sorted(list(set([int(input()) for _ in range(n)])))

dp = [float("inf")] * (k+1)
for coin in coins:
    if coin < k: dp[coin] = 1
    else: break

for coin in coins:
    cur = coin
    while cur+coin <= k:
        dp[cur+coin] = min(dp[cur+coin], dp[cur]+1)
        cur += 1
        
if dp[-1] == float("inf"): print(-1)
else: print(dp[-1])