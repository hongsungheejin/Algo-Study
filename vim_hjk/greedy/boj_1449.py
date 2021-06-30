import heapq

N, L  = map(int, input().split())

location = sorted(list(map(int, input().split())))
result = []
heapq.heappush(result, location.pop(0))

for loc in location:
    if loc - result[-1] > L - 1:
        heapq.heappush(result, loc)

# print(result)
print(len(result))