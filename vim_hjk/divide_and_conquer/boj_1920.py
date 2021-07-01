import sys


input = sys.stdin.readline

N = int(input())
data = list(map(int, input().split()))
data.sort()
M = int(input())
targets = list(map(int, input().split()))

def binary_search(target, data):    
    start = 0
    end = len(data) - 1

    while start <= end:
        mid = (start + end) // 2
        if data[mid] == target:
            return 1
        elif data[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return 0

for target in targets:
    print(binary_search(target, data))