import sys
from collections import Counter
input = sys.stdin.readline

N, H = map(int, input().split())
up = [0] * H
down = [0] * H

for n in range(N):
    height = int(input())
    
    if n%2==0: up[height-1] += 1
    else: down[height-1] += 1
    
for i in range(H-2, -1, -1):
    up[i] += up[i+1]
    down[i] += down[i+1]

min_break = float('inf')
breaks = [0] * H
for h in range(H):
    breaks[h] = up[h] + down[H-h-1]
    min_break = min(breaks[h], min_break)

cnt = Counter(breaks)
print(min_break, cnt[min_break])