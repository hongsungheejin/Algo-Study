N = int(input())
cherry = list(map(int, input().split()))

ans = 0
first, second, third, forth = 1, 1, 1, 1
for i in range(N-3):
    first *= cherry[i]
    
    second, third, forth = 1, 1, 1
    for j in range(i+1, N-2):
        second *= cherry[j]
        
        third = 1
        for k in range(j+1, N-1):
            third *= cherry[k]
            
            forth = 1
            for h in range(k+1, N):
                forth *= cherry[h]

            ans = max(ans, first+second+third+forth)
print(ans)