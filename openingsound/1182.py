n, k = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0


def dfs(node, sum):
    global n, ans
    if node != -1:
        if sum == k:
            ans += 1

    for i in range(node+1, n):
        dfs(i, sum + arr[i])


dfs(-1, 0)
print(ans)
