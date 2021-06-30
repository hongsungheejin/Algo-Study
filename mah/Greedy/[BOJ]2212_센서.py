N = int(input())
K = int(input())
coords = set(list(map(int, input().split())))
coords = sorted(list(coords))


if K >= N:
    print(0)
    exit()
else:
    dists = []
    for i in range(1, len(coords)):
        dists.append(coords[i] - coords[i-1])

    dists.sort()
    for i in range(K-1):
        dists.pop()
    print(sum(dists))