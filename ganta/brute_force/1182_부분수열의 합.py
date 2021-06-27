if __name__ == '__main__':
    N , S = list(map(int,input().split()))
    num_list = list(map(int, input().split()))
    ans = 0

    for check in range(1, 2**N):
        temp = 0
        for i in range(N):
            if check % 2 == 1: temp += num_list[i]
            check = check >> 1
        if temp == S:
            ans += 1
    
    print(ans)