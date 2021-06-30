N, K = map(int, input().split())

coins = []

for i in range(N):
  coins.append(int(input()))

coins = sorted(coins, reverse=True)
counts = []

for coin in coins:
  if coin > K:
    continue
  count, K = divmod(K, coin)
  counts.append(count)

  if K == 0:
    break

print(sum(counts))