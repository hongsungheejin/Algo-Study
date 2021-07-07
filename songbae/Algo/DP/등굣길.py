def solution(m,n,puddels):
  answer=0
  puddle=set([(i,j) for i,j in puddels])
  dp=[[0]*101 for i in range(101)]
  for i in range(m+1):
    for j in range(n+1):
      if (i,j) in puddle:dp[i][j]=0
      dp[i][j]+=dp[i-1][j]+dp[i][j-1]
  answer=dp[m][n]
  return answer