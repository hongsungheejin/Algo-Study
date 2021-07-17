from bisect import bisect_left

if __name__ == '__main__':
    N = int(input())
    num_arr = list(map(int, input().split()))
    
    res =[]
    loaction_indexes = []
    
    for i,num in enumerate(num_arr):
        insert_idx = bisect_left(res,num)
        loaction_indexes.append(insert_idx)
        
        if insert_idx == len(res):
            res.append(num)
        else:
            res[insert_idx] = num
            
    print(max(loaction_indexes) + 1)
    answers = []
    check = max(loaction_indexes)
    loaction_indexes.reverse()
    for i, li in enumerate(loaction_indexes):
        if li == check:
            answers.append(num_arr[len(num_arr) - (1 + i)])
            check -= 1
    answers.reverse()
    print(*answers)