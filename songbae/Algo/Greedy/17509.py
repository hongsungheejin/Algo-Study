from itertools import permutations
arr = sorted([list(map(int, input().split())) for i in range(11)])
answer = 0
T = 0
for d, v in arr:
    T += d
    answer += T+20*v
print(answer)
