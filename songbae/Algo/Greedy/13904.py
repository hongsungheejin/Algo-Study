import heapq
n = int(input())
temp = [[] for i in range(1002)]
for i in range(n):
  i,cnt=map(int,input().split())
  temp[i].append(cnt)
answer = list()
for i in range(1000+1):
    for idx,j in enumerate(temp[i]):
        if len(answer) < i:
            heapq.heappush(answer,j)
        elif answer[0] < j and len(answer)<=i:
                heapq.heappop(answer)
                heapq.heappush(answer,j)
print(sum(answer))
