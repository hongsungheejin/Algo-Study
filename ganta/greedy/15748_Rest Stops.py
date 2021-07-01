# import sys
# input = sys.stdin.readline

# if __name__ == '__main__':
#     L, N, rf, rb = map(int, input().split())
#     rest_list = []
#     for _ in range(N):
#         rest_list.append(list(map(int,input().split())))
    
#     rest_list.sort(key = lambda x : -x[1])
#     ans = 0
#     current_location = 0
#     rest_duration = rf - rb
    
#     for rest in rest_list:
#         if current_location < rest[0]:
#             ans += rest[1] * rest_duration * (rest[0] - current_location)
#             current_location = rest[0]
#     print(ans)


l, n, f, b = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(n)]
arr = sorted(arr, key=lambda x: -x[1])
answer = 0
now_time = 0
for dist, value in arr:
    time = dist*b+now_time
    if dist*f<=time :
      continue
    answer += value*(dist*f-time)
    now_time += dist*f-time
print(answer)