T = 1
while True:
    L, P, V = map(int, input().split())
    
    if L==0 and P==0 and V==0: break
    else:
        #  연속하는 P일 중 L일동안만 사용가능
        div = V//P
        res = V%P
        
        ans = div * L + min(res, L)
        print(f"Case {T}: {ans}")
        T+=1