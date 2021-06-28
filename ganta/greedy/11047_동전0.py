if __name__ == '__main__':
    N, K =  map(int, input().split())
    coin_list = []
    ans = 0
    
    for _ in range(N):
        coin_list.append(int(input()))
    
    for i in range(len(coin_list)-1, -1, -1):
        ans += K // coin_list[i]
        K = K % coin_list[i]
    
    print(ans)