def solution(rows,columns, swipes):
  arr=[[i*columns + j for j in range(1,columns+1)] for  i in range(rows)]
  total=list()
  for swipe in swipes:
    d,x1,c1,x2,c2=swipe
    answer=0
    temp=[[0]*(c2-c1+1) for i in range(x2-x1+1)]
    for idx,i in enumerate(range(x1-1,x2)):
      for jdx,j in enumerate(range(c1-1,c2)):
        if d==3:
          if jdx+1==len(temp[0]):answer+=arr[i][j]
          temp[idx][(jdx+1)%len(temp[0])]=arr[i][j]
        elif d==4:
          if jdx==0:answer+=arr[i][j]
          temp[idx][jdx-1] = arr[i][j]
        elif d==1:
          if idx+1==len(temp):answer+=arr[i][j]
          temp[(idx+1)%len(temp)][jdx] = arr[i][j]
        elif d==2:
          if idx==0 : answer+=arr[i][j]
          temp[idx-1][jdx] = arr[i][j]
    total.append(answer)
    for idx, i in enumerate(range(x1-1, x2)):
      for jdx, j in enumerate(range(c1-1, c2)):
        arr[i][j]=temp[idx][jdx]
  return total
rows=4
columns=3
swipes=[[1,1,2,4,3],[3,2,1,2,3,],[4,1,1,4,3],[2,2,1,3,3]]
for i in solution(rows,columns,swipes):
  print(i)
