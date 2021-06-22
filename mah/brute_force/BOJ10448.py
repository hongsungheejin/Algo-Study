import sys
from itertools import combinations_with_replacement
input = sys.stdin.readline

T = int(input())
nums = [(n+1)*n//2 for n in range(1, 46)]

while T:
    tar = int(input())
    
    combis = combinations_with_replacement(nums, 3)
    for combi in combis:
        if sum(combi) == tar:
            print(1)
            break
    else:
        print(0)
        
    T -= 1