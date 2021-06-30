problem = [list(map(int, input().split())) for _ in range(11)]

problem = sorted(problem, key=lambda x:(x[0], x[1]))
total_penalty = 0

t= 0
for d, v in problem:
    t += d
    total_penalty += (t + 20 * v)

print(total_penalty)