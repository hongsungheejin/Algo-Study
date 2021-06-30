import heapq
from collections import deque
import sys
MAX=1000000
input=sys.stdin.readline
n,k= map(int,input().split())
arr=[list(map(int,input().split()))for i in range(n)]
bag=sorted([int(input()) for i in range(k)])
temp=[[] for i in range(1000001)]
for i,cnt in arr:
  temp[i].append(cnt)
cnt=0
prev=min(MAX,bag[cnt])
now=list()
answer=0
flag=False
for j in range(MAX+1):
  if flag:break
  for k in temp[j]:# 30만번 돌고
    heapq.heappush(now,-k)
  while j==prev:
    if now:
      answer-= heapq.heappop(now)
    cnt+=1
    if cnt == len(bag):
      flag = True
      break
    prev = min(MAX, bag[cnt])
print(answer)
  





