import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
homework_list = sorted([list(map(int, input().split())) for _ in range(N)], key=lambda x:(-x[0], -x[1]))
homework_list = deque(homework_list)

day = 0
final = 0

#print(homework_list)
compare = homework_list.popleft()
final += compare[1]

while homework_list:    
    print(final, homework_list)    
    target = homework_list.popleft()
    if not homework_list: final += target[1]
    if compare[0] == target[0]:
        min_value = target[1]
        for idx, (time, score) in enumerate(homework_list):
            if score < min_value:
                min_value = score        
        if min_value < target[1]:
            del homework_list[idx]
            final += target[1]
            compare = target
    else:
        final += target[1]
        compare = target

print(final)