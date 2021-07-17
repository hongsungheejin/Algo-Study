n,m =map(int,input().split())
arr= [input() for i in range(n)]
temp=[[0]*m for i in range(n)]
flag=True
for i in range(n):
  for j in range(m):
    if arr[i][j]=='1':
      temp[i][j]=1
      flag=False

answer= 0 if flag else 1
for i in range(n):
  for j in range(m):
    if i==0 or j==0 : continue
    if arr[i-1][j]=='1' and arr[i][j-1]=='1' and arr[i-1][j-1]=='1' and arr[i][j]=='1':
      temp[i][j]=min(temp[i-1][j],temp[i][j-1],temp[i-1][j-1])+1
    answer=max(temp[i][j],answer)
# for i in temp:
#   print(i)
print(answer**2)
