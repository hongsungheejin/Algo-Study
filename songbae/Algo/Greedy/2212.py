n = int(input())
k = int(input())
arr = set(map(int, input().split()))
arr = sorted(list(arr))
temp = list()
prev = -1
if len(arr)==1:
  print(0)
  exit()
for idx, i in enumerate(arr):
    if prev == -1:
        prev = i
        continue
    temp.append(i-prev)
    prev=i
temp=sorted(temp)
for i in range(k-1):
  temp.pop()
print(sum(temp))

