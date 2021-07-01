N, K = list(map(int, input().split()))
coins = [int(input()) for _ in range(N)]

ans = 0
for i in range(N-1, -1, -1):
    if coins[i] <= K:
        ans += (K // coins[i])
        K %= coins[i]

print(ans)