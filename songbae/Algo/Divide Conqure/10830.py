n,b=map(int,input().split())
arr=[list(map(int,input().split())) for i in range(n)]

def matmul(x,y):
  result=[[0]*n for i in range(n)]
  for i in range(n):
    for j in range(n):
      for k in range(n):
        result[i][j]+=(x[i][k]*y[k][j])
      result[i][j]%=1000
  return result

def conq(start,end):
  if end==1:
    result=[[0]*n for i in range(n)]
    for i in range(n):
      for j in range(n):
        for k in range(n):
          result[i][j]+=(arr[i][k]*arr[k][j])
        result[i][j] %=1000
    return result
  elif end%2==1:
    result=conq(start,end-1)
    n_result=matmul(start,result)
    return n_result
  else:
    result=conq(start,end//2)
    n_result=matmul(result,result)
    return n_result
res=conq(0,b)
for i in res:
  print(*i)
  



