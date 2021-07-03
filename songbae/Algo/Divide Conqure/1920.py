n=int(input())
arr=sorted(list(map(int,input().split())))
k=int(input())
temp=list(map(int,input().split()))

def binary_search(x):
  start=0
  end=len(arr)-1
  while start<=end:
    mid=(start+end)//2
    if x==arr[mid]:return 1
    elif arr[mid]>x:end=mid-1
    else: start=mid+1
  return 0
for i in temp:
  print(binary_search(i))

