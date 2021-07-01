def calc(num_list, n):
    res = 0
    
    for num in num_list:
        res += (num // n)
    return res
    
if __name__ == '__main__':
    K, N = list(map(int, input().split()))
    num_list = []
    
    for _ in range(K):
        num_list.append(int(input()))
    
    max_len = max(num_list)

    start = 0
    end = max_len
    mid = 0
    ans = -1
    
    while start <= end:
        mid = (start + end) // 2
        check_num = calc(num_list, mid)       

        if check_num < N:
            end = mid - 1
        else:
            ans = mid
            start = mid + 1
    print(ans)
    