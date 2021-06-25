from itertools import permutations

if __name__ == '__main__':
    N = int(input())
    check_list = []
    pick_list = [str(i) for i in range(1,10)]
    res = 0

    for _ in range(N):
        a, b, c = list(map(int, input().split()))
        check_list.append([a,b,c])
    
    for pick in permutations(pick_list,3):
        flag = True

        for check in check_list:
            num, strike, ball = check
            num = list(str(num))

            # strike개수
            cnt = 0
            for i in range(3):
                if num[i] == pick[i]: cnt += 1
            if cnt != strike:
                flag = False
                break

            # ball개수
            cnt = 0
            for i in range(3):
                if num.count(pick[i]) != 0: cnt += 1
            if cnt != strike + ball:
                flag = False
                break
        
        if flag:
            res += 1

    print(res)