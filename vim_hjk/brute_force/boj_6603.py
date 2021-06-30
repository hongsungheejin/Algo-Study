from itertools import combinations
from collections import deque

lotto = deque()

while True:
  case = list(map(int, input().split()))
  if case[0] == 0: break
  else: lotto.append(case)

while True:
  case = lotto.popleft()
  for answer in combinations(case[1:], 6):
    print(*answer)
  if not lotto: break
  print()