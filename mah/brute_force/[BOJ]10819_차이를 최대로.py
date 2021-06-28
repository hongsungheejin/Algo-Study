from itertools import permutations

N = int(input())
nums = list(map(int, input().split()))
permus = permutations(nums, N)

ans = 0
for perm in permus:
    sub_sum = 0
    for i in range(1, N):
        sub_sum += abs(perm[i] - perm[i-1])
    
    ans = max(ans, sub_sum)
print(ans)