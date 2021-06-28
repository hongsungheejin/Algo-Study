N = int(input())
nums = sorted(list(map(int, input().split())))
M = int(input())
tars = list(map(int, input().split()))

def binary_search(tar):
    global nums
     
    l, r = 0, len(nums)-1
    
    while l <= r:
        m = (l+r)//2
        
        if nums[m] > tar: r = m - 1
        elif nums[m] < tar: l = m + 1
        else: return 1
    return 0
            
for tar in tars:
    print(binary_search(tar))