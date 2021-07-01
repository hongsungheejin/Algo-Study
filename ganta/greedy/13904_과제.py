import heapq

if __name__ == "__main__":
    N = int(input())
    infos = []
    for _ in range(N):
        day, score = map(int, input().split())
        infos.append([day, score])
        
    heap = []
    infos.sort(key = lambda x  : x[0])
    
    for d in range(1,infos[-1][0] + 1):
        while len(infos) != 0 and infos[0][0] <= d:
            info = infos.pop(0) 
            if len(heap) != d:
                heapq.heappush(heap,info[1])
            else:
                if heap[0] < info[1]:
                    heapq.heappop(heap)
                    heapq.heappush(heap, info[1])
    
    print(sum(heap))