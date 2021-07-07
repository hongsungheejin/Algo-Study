n,k=map(int,input().split())
k=min(n-k,k)
answer=1
MAX=10007
for i in range(k):
  answer*=(n-i)
  answer//=(i+1)
print(answer)
  
