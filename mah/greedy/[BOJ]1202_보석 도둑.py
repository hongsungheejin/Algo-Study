import sys, heapq
input = sys.stdin.readline

N, K = list(map(int, input().split()))
jewelry = [[] for _ in range(1000001)] 
for _ in range(N):
    weight, value = list(map(int, input().split()))
    jewelry[weight].append(-value)
bags = sorted([int(input()) for _ in range(K)])

ans = 0
min_bag = -1
candis = []
for bag in bags:
    for idx in range(bag, min_bag, -1):
        for item in jewelry[idx]:
            heapq.heappush(candis, item)
    
    min_bag = bag
    if candis:
        ans -= heapq.heappop(candis)
        
print(ans)