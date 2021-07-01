import sys
import heapq

input = sys.stdin.readline

if __name__ ==  "__main__":
    N , K  = map(int, input().split())
    jewerlies = []
    bags = []
    heap= []
    for _ in range(N):
        jewerlies.append(list(map(int, input().split())))
    for _ in range(K):
        bags.append(int(input()))
    
    jewerlies.sort(key= lambda x : -x[0])
    bags.sort()
    ans = 0
    
    for bag in bags:
        while len(jewerlies) != 0:
            if bag < jewerlies[-1][0]: break
            search_j = jewerlies.pop()
            heapq.heappush(heap, -search_j[1])
        if heap:
            ans += -heapq.heappop(heap)
    print(ans)
