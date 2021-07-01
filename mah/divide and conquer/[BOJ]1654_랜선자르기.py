from sys import stdin
input = stdin.readline

K, N = list(map(int, input().split()))
cables = [int(input()) for _ in range(K)]


def binary_serach():
    l, r = 1, max(cables)
    ans = 0
    
    while True:
        if l > r: return l-1
        
        m = (l+r)//2
        
        cnt = 0
        for cable in cables:
            cnt += cable // m
            
        if cnt < N:
            r = m - 1
        else:
            l = m + 1
            ans = m
            
    return ans
    
print(binary_serach())