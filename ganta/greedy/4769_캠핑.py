if __name__ == '__main__':
    cnt = 1
    
    while True:
        L, P, V = map(int, input().split())
        
        if L == 0 and P == 0 and V == 0:
            break
        
        ans1 = L * (V // P)
        ans2 = V % P
        if ans2 > L:
            ans2 = L
        
        print(f"Case {cnt}: {ans1 + ans2}")
        cnt += 1
         
        