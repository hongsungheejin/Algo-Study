n,r,c=map(int,input().split())
answer=0
def con(x,y,size):
  global answer
  cnt=size**2
  if x<=r and r<x+size and y<=c and c<y+size:
    answer+=cnt*0
    con(x,y,size//2)
  elif x<=r and r<x+size and y+size<=c and c<y+2*size:
    answer+=cnt*1
    con(x, y+size, size//2)
  elif x+size<=r and r<x+size*2 and y<=c and c<y+size:
    answer+=cnt*2
    con(x+size, y, size//2)
  else:
    answer+=cnt*3
    con(x+size, y+size, size//2)
  return

con(0,0,1<<(n-1))
print(answer)