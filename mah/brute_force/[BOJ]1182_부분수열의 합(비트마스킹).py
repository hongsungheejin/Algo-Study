N, S = list(map(int, input().split()))
nums = list(map(int, input().split()))

count = 0
maxBit = 2**N
for bit in range(1, maxBit):
    sub_sum = 0
    
    for j in range(N):
        if bit & (1<<j):
            sub_sum += nums[j]
    
    if sub_sum == S:
        count += 1
    
print(count)