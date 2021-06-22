from itertools import combinations
short = sorted(int(input()) for i in range(9))
for i in combinations(short, 7):
    if sum(i) == 100:
        for k in i:
            print(k)
        break
