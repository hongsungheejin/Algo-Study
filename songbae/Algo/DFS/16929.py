from collections import deque
n, m = map(int, input().split())
arr = [input() for i in range(n)]
unique_alpa=set()
for i in arr:
  for j in i:
    unique_alpa.add(j)
temp=[]
for k in unique_alpa:
    flag=True
    for idx in range(len(arr)):
        if not flag:break
        for jdx in range(len(arr[0])):
            if arr[idx][jdx] == k:
              temp.append([idx,jdx])
              flag=False
              break
visit = [[0]*m for i in range(n)]
for idx,jdx in temp:
  k=arr[idx][jdx]
  deq = deque()
  visit[idx][jdx] = 1
  deq.append((idx, jdx,idx,jdx, 1))
  while deq:
      x, y, b_x,b_y,cnt = deq.pop()
      for p in range(4):
          nx = x+int('1201'[p])-1
          ny = y+int('2110'[p])-1
          if nx < 0 or ny < 0 or nx >= n or ny >= m:continue
          if arr[nx][ny] != k:continue

          if visit[nx][ny]>=1 and (nx!=b_x or ny!=b_y) and  cnt!=visit[nx][ny]-1:
              print('Yes')
              exit()
          if visit[nx][ny]:
              continue
          visit[nx][ny] = cnt+1
          deq.append((nx, ny,x,y, cnt+1))                   
print('No')
