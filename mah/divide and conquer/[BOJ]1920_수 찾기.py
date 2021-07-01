N = int(input())
nums = list(map(int, input().split()))
nums.sort()

M = int(input())
tars = list(map(int, input().split()))


def binary_serach(tar):
    l, r = 0, len(nums) - 1
    
    while l<=r:
        m = (l+r)//2
        
        if nums[m] == tar: return 1
        elif nums[m] < tar: l=m+1
        else: r=m-1
    return 0    


for tar in tars:
    print(binary_serach(tar))