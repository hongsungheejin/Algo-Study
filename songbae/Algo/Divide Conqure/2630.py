n= int(input())
arr=[list(map(int,input().split())) for i in range(n)]
w,b=0,0

def search(x,y,size):
  cnt=0
  for i in range(x,x+size):
    for j in range(y,y+size):
      if arr[i][j]:cnt+=1
  return cnt
  
def div_conq(x,y,size):
  global w,b
  cnt=search(x,y,size)
  if not cnt: w+=1
  elif cnt==size**2:b+=1
  else:
    nsize=size//2  
    div_conq(x,y,nsize)
    div_conq(x, y+nsize, nsize)
    div_conq(x+nsize, y, nsize)
    div_conq(x+nsize, y+nsize, nsize)
  return
div_conq(0,0,n)
print(w)
print(b)

