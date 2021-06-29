key = list()

for i in range(9):
  key.append(int(input()))

key = sorted(key)

fake1 = 0
fake2 = 0

for i in range(9):
  for j in range(1, 9):
    if sum(key) - key[i] - key[j] == 100:
      fake1, fake2 = i, j
      break

for i in range(9):
  if i == fake1 or i == fake2:
    continue
  print(key[i], end='\n')