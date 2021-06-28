import sys
input = sys.stdin.readline

n = int(input())
l = []
for i in range(n):
    a, b = map(int, input().split())
    l.append([a, b])

l.sort(key=lambda x: (x[1], x[0]))

started = 0
answer = 0

for a, b in l:
    if started <= a:
        answer += 1
        started = b

print(answer)
