
if __name__ == '__main__':
    K = int(input())
    arr = list(map(int, input().split()))
    
    dp = []

    for a in arr:
        dp.append(a)

    dp[0] = arr[0]

    for i in range(1,K):
        dp[i] = max(dp[i], dp[i-1] + arr[i])

    print(max(dp))

