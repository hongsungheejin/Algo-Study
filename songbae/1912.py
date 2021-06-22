n=int(input())
arr=list(map(int,input().split()))
sum=0
answer=arr[0]
for i in range(n):
  sum+=arr[i]
  answer=max(answer,sum )
  if sum<0:sum=0
print(answer)
  
 


