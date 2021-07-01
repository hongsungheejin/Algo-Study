N = int(input())

cur_t = 0
assignments = {}
for _ in range(N):
    d, w = list(map(int, input().split()))
    cur_t = max(cur_t, d)
    if d in assignments: assignments[d].append(w)
    else: assignments[d] = [w]


ans = 0
candis = []
while cur_t:
    candi = assignments.get(cur_t)
    if candi:
        candis.extend(candi)
        candis.sort()
    cur_t -= 1
    
    if not candis: continue
    else:
        ans += candis.pop()
print(ans)