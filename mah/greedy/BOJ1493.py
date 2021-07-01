# import math
# import sys
# sys.setrecursionlimit(1000000)

# l, w, h = list(map(int, input().split()))
# N = int(input())
# cubes = [[0, 0] for _ in range(20)]

# for _ in range(N):
#     i, num = list(map(int, input().split()))
#     cubes[i][0] += num
#     cubes[i][1] = (1 << i)


# flag = True
# def solve(l, w, h):
#     global cubes, flag
#     if not flag: return 0 
    
#     if (l == 0 or w == 0 or h == 0): return 0
#     else:
#         pos = int(math.log2(min(l, w, h)))
#         while pos >= 0:
#             if cubes[pos][0]: break
#             else:
#                 pos -= 1
        
#         if pos == -1:
#             flag=False
#             return 0
#         else:        
#             if cubes[pos][0]:
#                 cubes[pos][0] -= 1
                
#                 return solve(l-cubes[pos][1], cubes[pos][1], h) + \
#                        solve(l, w-cubes[pos][1], h) + \
#                        solve(cubes[pos][1], cubes[pos][1], h-cubes[pos][1]) + 1
                

# ans = solve(l, w, h)
# if flag: print(ans)
# else: print(-1)

l, w, h = list(map(int, input().split()))
N = int(input())
cubes = [0] * 20

for _ in range(N):
    i, num = list(map(int, input().split()))
    cubes[i] += num

ans = 0
add = 0
vol = l * w * h
for i in range(19, -1, -1):
    cube_size = ((1 << i) ** 3)
    add_cube = min((vol - add) // cube_size, cubes[i])
    add += add_cube * cube_size
    ans += add_cube
    
if add == vol:print(ans)
else: print(-1)