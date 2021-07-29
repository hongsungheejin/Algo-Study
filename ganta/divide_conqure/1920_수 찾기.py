if __name__ == '__main__':
    N = int(input())
    num_list = list(map(int, input().split()))
    M = int(input())
    search_list = list(map(int, input().split()))
    
    num_list.sort()
    
    for search in search_list:
        flag = False
        
        start = 0
        end = len(num_list) - 1
        
        while start <= end:
            mid = (start + end) // 2
            check_num = num_list[mid]
            
            if check_num == search:
                flag= True
                break
            elif check_num > search:
                end = mid - 1
            else:
                start = mid + 1
        
        if flag:
            print(1)
        else:
            print(0)