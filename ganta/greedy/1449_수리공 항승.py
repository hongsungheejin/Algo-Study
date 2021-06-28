if __name__ == '__main__':
    N, L = map(int, input().split())
    num_arr = list(map(int, input().split()))
    
    num_arr.sort()
    
    temp = []
    ans = 0
    dist = 0
    
    for num in num_arr:
        if len(temp) == 0:
            temp.append(num)
            continue
        
        dist += num - temp[-1]
        
        if dist <= (L - 1):
            temp.append(num)
            continue
        
        if dist > (L - 1):
            ans += 1
            dist = 0
            temp = []
            temp.append(num)
            
    print(ans + 1)
