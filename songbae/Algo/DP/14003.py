import bisect
n=int(input())
arr=list(map(int,input().split()))
answer=list()
temp=list()
ans=list()
p=0
for k,i in enumerate(arr):
  if not answer:
    answer.append(i)
    temp.append((i,0))
    continue
  if answer[-1]<i:
    answer.append(i)
    temp.append((i,len(answer)-1))
    p=max(len(answer)-1,p)
    ans=ans 
  else:
    idx=bisect.bisect_left(answer,i)
    temp.append((i,idx))
    answer[idx]=i
for k,i in temp[::-1]:
  if i ==p:
    ans.append(k)
    p-=1

print(len(answer))
print(*reversed(ans))
    
