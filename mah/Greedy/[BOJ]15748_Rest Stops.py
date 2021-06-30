import sys
input = sys.stdin.readline

L, N, rF, rB = list(map(int, input().split()))
tastiness = [list(map(int, input().split())) for _ in range(N)]
tastiness = sorted(tastiness, key=lambda x: -x[1])

ans = 0
prev_rest = 0
cur_time = 0
for dist, value in tastiness:
    if prev_rest > dist: continue
    
    bessie_t, john_t = dist * rB, dist * rF
    rest_t =  john_t - bessie_t
    
    ans += (rest_t - cur_time) * value
    cur_time = rest_t
    prev_rest = dist
    
print(ans)