import sys
input = sys.stdin.readline

N = int(input())
times = [list(map(int, input().split())) for _ in range(N)]
times = sorted(times, key=lambda x: (x[1], x[0]))
ans = 0
start = 0
for n in range(N):
    if times[n][0] >= start:
        ans += 1
        start = times[n][1]

print(ans)