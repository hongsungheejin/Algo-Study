from itertools import permutations

def calculate(n, example):
  result = 0
  for i in range(1, n):
    result += abs(example[i - 1] - example[i])
  return result

n = int(input())

number = list(map(int, input().split()))

answer = -1

for example in permutations(number, n):
  answer = max(answer, calculate(n, example))

print(answer)