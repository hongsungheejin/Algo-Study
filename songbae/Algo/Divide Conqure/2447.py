import sys 
n=int(input())
arr=[[' ']*n for i in range(n)]
def conq(size,x,y):
  if size==1:
    arr[x][y]="*"
    return 
  n_size=size//3
  for i in range(3):
    for j in range(3):
      if j==1 and i==1:continue
      conq(n_size,x+n_size*i, y+n_size*j)
  return

conq(n,0,0)
for i in arr:
  print(*i)
