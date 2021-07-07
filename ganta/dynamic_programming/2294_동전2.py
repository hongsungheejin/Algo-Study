if __name__ == '__main__':
    n, k = list(map(int, input().split()))
    coin_list = []
    
    for _ in range(n):
        coin_list.append(int(input()))
    
    coint_list = list(set(coin_list))    
    
    dp = [10005] * (k+1)
    dp[0] = 0
    
    for coin in coin_list:
        for j in range(coin, k + 1):
            dp[j] = min(dp[j], dp[j - coin] + 1)
            
        
    if dp[-1] == 10005:
        print(-1)
    else:
        print(dp[-1])
            
            
        