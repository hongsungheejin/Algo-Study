from itertools import combinations
n = int(input())
temp = [int(input()) for i in range(n)]
t = [0]*46
for i in range(1, 46):
    t[i] = t[i-1]+i

answer = set()
t = t[1:]*3
for i in combinations(t, 3):
    answer.add(sum(i))

for i in temp:
    if i in answer:
        print(1)
    else:
        print(0)
