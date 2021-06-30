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
