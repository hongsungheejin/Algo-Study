n=int(input())
arr=[list(map(int,input().split())) for i in range(n)]
arr.sort(key=lambda x: (x[1],x[0]))
prev=-1
cnt=0
for i,j in arr:
  if prev==-1:
    prev=j
    cnt+=1
  else:
    if prev<=i:
      cnt+=1
      prev=j
print(cnt)


