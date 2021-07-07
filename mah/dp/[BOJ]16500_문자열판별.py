import sys
from collections import deque
input = sys.stdin.readline

S = input().strip()
A = int(input())
words = list(set([input().strip() for _ in range(A)]))

que = deque([word for word in words if S[:len(word)]==word])
check = [False] * len(S)
while que:
    cur_string = que.popleft()
    cur_size = len(cur_string)
    
    if cur_size == len(S):
        print(1)
        exit()
    
    for word in words:
        nxt_string = cur_string + word
        
        if len(nxt_string) > len(S): continue
        if check[len(nxt_string)-1]: continue
        for idx in range(cur_size, cur_size+len(word)):
            if S[idx] != word[idx-cur_size]: break
        else:
            que.append(nxt_string)
            check[len(nxt_string)-1] = True
        
print(0)

# size = len(S)
# dp = [0] * 101
# dp[size] = 1

# for pos in range(size-1, -1, -1):
#     for word in words:
#         if pos+len(word) <= size and S[pos:pos+len(word)] == word and dp[pos+len(word)] == 1:
#             dp[pos] = 1
#             break
#         else:
#             dp[pos] = 0

# print(dp[0])