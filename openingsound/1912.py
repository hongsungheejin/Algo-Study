n = int(input())

arr = list(map(int, input().split()))
ans = -10000
pre_sum = 0
for i in range(len(arr)):
    pre_sum = max(arr[i] + pre_sum, arr[i])
    ans = max(ans, pre_sum)
print(ans)
