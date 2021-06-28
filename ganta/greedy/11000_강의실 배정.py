import sys
input = sys.stdin.readline
import heapq

if __name__ == '__main__':
    N = int(input())
    class_list = []
    
    heap = []
    ans = 0
    
    for _ in range(N):
        class_list.append(list(map(int,input().split())))
    
    class_list.sort(key = lambda x : x[0])
    for start, end in class_list:
        
        if len(heap) == 0:
            heapq.heappush(heap, end)
            continue
            
        while True:
            if len(heap) == 0 or heap[0] > start:
                break
            heapq.heappop(heap)
        heapq.heappush(heap, end)
        ans = max(ans, len(heap))
        
    print(ans)