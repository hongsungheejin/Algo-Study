if __name__ == '__main__':
    N = int(input())
    budget = list(map(int, input().split()))
    M = int(input())
    
    start, end = 0, max(budget)
    

    while start <= end:
        mid = (start + end) // 2
        
        total = 0
        for i in budget:
            total += min(mid, i)
        
        # 예산을 넘어가면 줄이기
        if total > M:
            end = mid - 1
        # 예산을 넘어가지 않으면 늘리기
        else:
            start = mid + 1
    print(end)
                
        