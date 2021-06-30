from itertools import product

t = int(input())
k = list()
for i in range(t):
  k.append(int(input()))

triangle = list()

for i in range(1, 1001):
  if (i * (i + 1) // 2) > 1000:
    break
  else: triangle.append((i * (i + 1) // 2))

for i in k:
  check = 0
  for j in product(triangle, repeat=3):
    if sum(j) == i:
      check = 1      
      break
  print(check)