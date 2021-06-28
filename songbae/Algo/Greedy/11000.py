import sys
input = sys.stdin.readline
n = int(input())
arr = [list(map(int, input().split()))for i in range(n)]
x = set()
for i,j in arr:
  x.add(i)
  x.add(j)
x= list(x)
x.sort()
dict_x = {i: idx for idx, i in enumerate(x)}
sub = list()
for i, j in arr:
    sub.append([dict_x[i], dict_x[j]])
temp = [0]*400001
for i, j in sub:
    temp[i] += 1
    temp[j] -= 1
answer = 0
for i in range(1, 400001):
    temp[i] = temp[i-1]+temp[i]
    answer=max(temp[i],answer)
print(answer)
