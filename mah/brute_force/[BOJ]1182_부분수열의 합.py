from itertools import combinations

N, S = list(map(int, input().split()))
nums = list(map(int, input().split()))

count = 0
for i in range(1, N+1):
    combis = combinations(nums, i)
    
    for combi in combis:
        if sum(combi) == S: count += 1
print(count)