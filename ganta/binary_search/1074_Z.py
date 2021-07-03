import sys

res = 0
R = 0
C = 0
cnt = 0

input = sys.stdin.readline

def check(r,c,n):
    global cnt
    
    if n == 2:
        for i in range(r, r + 2):
            for j in range(c, c+2):
                if i == R  and j == C:
                    print(cnt)
                    exit(0)
                cnt += 1
        return
    
    nr = r + n // 2
    nc = c + n // 2
    list1  = [i for i in range(r, nr)]
    list2 = [i for i in range(nr, r+n)]
    list3 = [i for i in range(c , nc)]
    list4 = [i for i in range(nc, c+n)]
    
    if R in list1 and C in list3:
        check(r,c,n//2)
    else:
        cnt += (n//2) ** 2
        
    if R in list1 and C in list4:
        check(r,nc, n//2)
    else:
        cnt += (n//2) ** 2
    
    if R in list2 and C in list3:    
        check(nr,c, n//2)
    else:
        cnt += (n//2)**2
    
    if R in list2 and C in list4:
        check(nr,nc,n//2)
    else:
        cnt += (n//2)**2

if __name__ == "__main__":
    N, R, C = map(int, input().split())
    N = 2**N

    check(0,0,N)
    