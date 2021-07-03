n=int(input())
arr= [list(map(int,input())) for i in range(n)]
answer=''
def div_con(x,y,size):
  global answer
  cnt=0
  for i in range(x,x+size):
    for j in range(y,y+size):
      if arr[i][j]:
        cnt+=1
  if cnt==size*size:
    answer+='1'
  elif cnt==0:
    answer+='0'
  else:
    nsize=size//2
    answer+='('
    div_con(x,y,nsize)
    div_con(x, y+nsize, nsize)
    div_con(x+nsize, y, nsize)
    div_con(x+nsize, y+nsize, nsize)
    answer+=')'
  return

div_con(0,0,n)
print(answer)