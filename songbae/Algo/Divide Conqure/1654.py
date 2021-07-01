import sys
input=sys.stdin.readline
n,k= map(int,input().split())
arr=[int(input()) for i in range(n)]
answer=0
def binary_search(x):
  global answer
  start = 1
  end = x
  while start <= end:
    mid = (start+end)//2
    sum=0
    for i in arr:
      sum+=i//mid
    if sum < k:
      end = mid-1
    else:
      answer = max(mid, answer)
      start = mid+1
binary_search(max(arr))
print(answer)

