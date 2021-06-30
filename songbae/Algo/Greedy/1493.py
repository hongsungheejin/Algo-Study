l, w, h = list(map(int, input().split()))
N = int(input())
cubes = [0] * 20

for _ in range(N):
    i, num = list(map(int, input().split()))
    cubes[i] += (1 << i) ** 3 * num
ans = 0
add = 0
vol = l * w * h
for i in range(19, -1, -1):
    add_vol = min(cubes[i], vol - add)
    add += add_vol

    add_cube = add_vol // ((1 << i) ** 3)
    ans += add_cube

if add == vol:
    print(ans)
else:
    print(-1)
