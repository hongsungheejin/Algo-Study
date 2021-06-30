import sys

N = int(input())

time_table = []
cur_time = -1
count = 0

for _ in range(N):
  time_table.append(list(map(int, sys.stdin.readline().split())))

time_table = sorted(time_table, key=lambda x:(x[1], x[0]))

for t in time_table:
  if t[0] >= cur_time:
    count += 1
    cur_time = t[1]

print(count)