time, penalty = 0, 0
inps = sorted([list(map(int, input().split())) for _ in range(11)])

for inp in inps:
    time += inp[0]
    penalty += (time +20 * inp[1])
    
print(penalty)