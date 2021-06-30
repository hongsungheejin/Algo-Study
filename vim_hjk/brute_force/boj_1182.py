from itertools import combinations

n, s = map(int, input().split())
number = list(map(int, input().split()))

answer = 0

for sub_num in range(1, n + 1):
  for p in combinations(number, sub_num):
    if sum(p) == s:
      answer += 1

print(answer)