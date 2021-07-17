from itertools import combinations

n=int(input())
arr=list(map(int,input().split()))
answer=0
for comb in combinations([i+1 for i in range(len(arr)-1)],3):
  g1,g2,g3,g4=1,1,1,1
  a,b,c=comb
  for i in range(0,a):
    g1*=arr[i]
  for j in range(a,b):
    g2*=arr[j]
  for k in range(b,c):
    g3*=arr[k]
  for p in range(c,len(arr)):
    g4*=arr[p]
  answer=max(answer,g1+g2+g3+g4)

print(answer)
  