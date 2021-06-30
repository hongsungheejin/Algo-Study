if __name__ == '__main__':
    N = int(input())
    K = int(input())
    num_arr = list(set(map(int, input().split())))

    num_arr.sort()
    
    ans = 0
    dist_arr = []
    for i in range(0,len(num_arr) - 1):
        dist_arr.append(num_arr[i+1] - num_arr[i])
    
    dist_arr.sort(reverse=True)
    # 긴거 끊어주기
    for d in dist_arr[K-1:]:
        ans += d
    print(ans)