from collections import defaultdict

N, X = map(int, input().split())
visitors = [0] + list(map(int, input().split()))

if N == 1:
    print(visitors[0])
    print(1)
else:
    max_val = 0
    cnt = 1
    for i in range(1, N+1):
        visitors[i] += visitors[i-1]
        
        if i-X>=0:
            sub_val = visitors[i] - visitors[i-X]
            if sub_val == max_val: cnt += 1
            elif max_val < sub_val:
                cnt = 1
                max_val = sub_val

    if max_val == 0: print("SAD")
    else:
        print(max_val)
        print(cnt)