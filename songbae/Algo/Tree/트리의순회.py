import sys 
sys.setrecursionlimit(10**6)
n=int(input())
inorder,postorder=[0],[0]
arr=[list(map(int,input().split()))for i  in range(2)]
inorder.extend(arr[0])
postorder.extend(arr[1])
inorder_idx= [0]*(n+1)# 이게 인오더 인덱스
for i in range(1,n+1):
  inorder_idx[inorder[i]]=i
def recur(st,end, st1,end1):
  if st>end or st1>end1:
    return
  root=postorder[end1]
  mid=inorder_idx[root-1]
  print(root,end=" ")
  recur(st,mid-1,st1,st1+mid-st-1)
  recur(mid+1,end,st1+mid-st,end1-1)
  return 
recur(1,n,1,n)
