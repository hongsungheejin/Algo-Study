import sys
from bisect import bisect_left
input = sys.stdin.readline

N = int(input())
nums = list(map(int,  input().split()))

seq = []
memory = []
for i, num in enumerate(nums):
    if not seq or nums[i] > seq[-1]:
        seq.append(num)
        memory.append((len(seq)-1, num))
    else:
        idx = bisect_left(seq, num)
        seq[idx] = num
        memory.append((idx, num))

ans = []
cur_idx = len(seq)-1
for i in range(len(memory)-1, -1, -1):
    if memory[i][0] == cur_idx:
        ans.append(memory[i][1])
        cur_idx -= 1

print(len(ans))
print(*reversed(ans))