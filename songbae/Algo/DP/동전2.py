import sys
input=sys.stdin.readline
n,k =map(int,input().split())
arr= list(set([int(input())for i in range(n)]))
arr.sort()
dp=[float('inf')]*10001
dp[0]=0
for i in range(k+1):
  for j in arr:
    if j>i:break
    dp[i]=min(dp[i-j]+1,dp[i])
print(dp[k] if dp[k]!=float('inf') else -1)

