import sys

input = sys.stdin.readline

N = int(input())
K = int(input())
coordinates = sorted(list(map(int, input().split())))

if N <= K: print(0)

else:
    distance = []
    for i in range(1, N):
        distance.append(coordinates[i] - coordinates[i - 1])

    distance = sorted(distance, reverse=True)

    for i in range(K - 1):
        distance.pop(0)

    print(sum(distance))