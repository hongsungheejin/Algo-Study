import sys

input = sys.stdin.readline

L, N, r_f, r_b = map(int, input().split())
rest_stops = sorted([list(map(int, input().split())) for _ in range(N)], key=lambda x:x[1], reverse=True)

cur_loc = 0
tastiness_units = 0

for i, (stop_loc, score) in enumerate(rest_stops):    
    if stop_loc > cur_loc:
        tastiness_units += ((r_f - r_b) * (stop_loc - cur_loc) * score)
        cur_loc = stop_loc

print(tastiness_units)