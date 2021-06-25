N = int(input())
nums = list(map(int, input().split()))

ans = 0
prev = nums[0]
for i in range(1, N):
    ans += prev * nums[i]
    prev += nums[i]
    
print(ans)