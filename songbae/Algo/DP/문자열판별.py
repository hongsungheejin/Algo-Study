from collections import deque
word=input()
n=int(input())
subwords=[input()for i in range(n)]
dp=[[]*101 for _ in range(200)]
for idx,i in enumerate(word):
  for j in subwords:
    if word[idx:idx+len(j)]==j:
      dp[idx].append(j)
answer=0
check = [[0]*101 for _ in range(200)]
def recur(cur,idx):
  global answer
  if idx>=len(word):
    if cur==word:
        
        answer=1
    return 

  for j,i in enumerate(dp[idx]):
    if check[idx][j]:continue
    check[idx][j]=True
    recur(cur+i,len(cur+i))
  return 
recur('',0)
print(answer)




