N = int(input())

query = []

for i in range(N):
  match = list(map(int, input().split()))
  query.append(match)

candidate = []

for i in range(111, 1000):
  if len(set(str(i))) == 3 and '0' not in str(i):
    candidate.append(i)



for pred, strike, ball in query:
  tmp = []
  for target in candidate:
    tmp_strike = 0
    tmp_ball = 0
    for p, t in zip(str(pred), str(target)):
      if p == t:
        tmp_strike += 1
      elif (p != t) and (t in str(pred)):
        tmp_ball += 1
    if tmp_strike == strike and tmp_ball == ball:
      tmp.append(target)
  candidate = tmp

#print(candidate)
print(len(candidate))