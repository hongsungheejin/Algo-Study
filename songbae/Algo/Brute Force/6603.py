# from itertools import combinations


# while 1:
#   arr=list(map(int, input().split()))[1:]
#   if not arr: break
#   for i in combinations(arr,6):print(*i)
#   print()


temp=list()
def Func(arr,idx):
  if 6==len(temp):
    print(*temp)
    return 
  for i in range(idx,len(arr)):
    temp.append(arr[i])
    Func(arr,i+1)
    temp.pop()
  return 

while 1:
  arr = list(map(int, input().split()))[1:]
  if not arr: break 
  Func(arr,0)
  print()
