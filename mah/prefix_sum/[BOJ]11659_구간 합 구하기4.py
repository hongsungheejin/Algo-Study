import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))
sums = [0]
for n in range(N):
    sums.append(sums[n] + nums[n])

for m in range(M):
    s, e = map(int, input().split())
    print(sums[e]-sums[s-1])