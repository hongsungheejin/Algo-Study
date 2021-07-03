import sys
input=sys.stdin.readline
n=int(input())
arr=[list(map(int,input().split()))for i in range(n)]
a,b,c=0,0,0

def search(x, y, size):
  plus,minus ,zero= 0,0,0
  for i in range(x, x+size):
    for j in range(y, y+size):
      if arr[i][j]==1:
        plus += 1
      elif arr[i][j]==-1:
        minus+=1
      else:
        zero+=1
  return plus,minus,zero

def div_conq(x, y, size):
  global a,b,c
  plus,minus,zero = search(x, y, size)
  need_size=size*size
  if plus==need_size:
    a+=1
  elif minus==need_size:
    b+=1    
  elif zero == need_size:
    c+=1
  else:
    nsize = size//3
    div_conq(x, y, nsize)
    div_conq(x, y+nsize, nsize)
    div_conq(x, y+nsize*2, nsize)
    div_conq(x+nsize, y, nsize)
    div_conq(x+nsize, y+nsize, nsize)
    div_conq(x+nsize, y+nsize*2, nsize)
    div_conq(x+nsize*2, y, nsize)
    div_conq(x+nsize*2, y+nsize, nsize)
    div_conq(x+nsize*2, y+nsize*2, nsize)
  return


div_conq(0, 0, n)
print(b)
print(c)
print(a)