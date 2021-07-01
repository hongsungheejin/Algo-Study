import sys


input = sys.stdin.readline

K, N = map(int, input().split())

lan_len = [int(input()) for _ in range(K)]

start = 1
end = max(lan_len)

while start <= end:
    mid = (start + end) // 2
    result = 0
    for l in lan_len:
        result += l // mid

    if result >= N:
        start = mid + 1
    else:
        end = mid - 1

print(end)