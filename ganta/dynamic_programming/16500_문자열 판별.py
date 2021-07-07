import sys
input = sys.stdin.readline

if __name__ == '__main__':
    search_str = input().strip()
    N = int(input())
    
    words  = []
    
    for _ in range(N):
        words.append(input().strip())
    
    dp = [0] * (len(search_str) + 1)
    dp[0] = 1

    for i in range(len(search_str)):
        if dp[i] == 0:
            continue
        
        for word in words:
            if search_str[i:].startswith(word): # bfs보다 빠름 -> 중복된 도착 지점 있을 때 한번에 처리 가능
                dp[i + len(word)] = 1
    
    if dp[len(search_str)] == 0:
        print(0)
    else:
        print(1)

"""bfs풀이"""
# import sys
# from collections import deque

# input = sys.stdin.readline

# if __name__ == '__main__':
#     search_str = input()[:-1]
#     N = int(input())
#     words  = []
#     for _ in range(N):
#         words.append(input()[:-1])

#     dq = deque()
#     dq.appendleft([search_str, 0])
#     res  = False
    
#     visited = [0] * (len(search_str) + 1)
#     visited[0] = 1
    
#     while dq:
#         search, start_point = dq.pop()
        
#         if len(search) == 0:
#             res = True
#             break
        
#         for word in words:
#             if search.startswith(word) and visited[start_point + len(word)] == 0:
#                 insert_str = search[len(word):]
#                 visited[start_point + len(word)] = 1
#                 dq.appendleft([insert_str, start_point + len(word)])
    
#     if res:
#         print(1)
#     else:
#         print(0)