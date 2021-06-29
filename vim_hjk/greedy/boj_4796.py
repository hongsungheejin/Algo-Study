answer = []

while True:    
    L, P, V = map(int, input().split())

    if L == 0 and P == 0 and V == 0: break

    possible, remainder = divmod(V, P)
    remainder = remainder if remainder <= L else L    

    answer.append(possible * L + remainder)
    
for i, v in enumerate(answer):
    print(f'Case {i + 1}: {v}')