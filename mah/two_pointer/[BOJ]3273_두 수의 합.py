n = int(input())
nums = sorted(list(map(int, input().split())))
x = int(input())

ans = 0
left = 0
right = len(nums) - 1
while left < right:
    asum = nums[left] + nums[right]
    if asum == x:
        ans += 1
        left += 1
    elif asum > x:
        right -= 1
    else:
        left += 1
    
print(ans)